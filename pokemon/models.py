from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
import requests
import json

# Create your models here.


class PokemonPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


# Create your models here.
class Pokemon(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default='default name')

    # not calculated, most come from a list of established names or numbers
    species = models.CharField(max_length=30, default='venusaur')
    number = models.CharField(max_length=30, default=3)

    # meta, doesnt change
    gender = models.CharField(
        choices=GENDER, max_length=1, default='M')

    # meta, will change
    evolutions = ArrayField(models.CharField(max_length=25, default=''), default="error")
    description = models.TextField(default="default")
    sprite = models.URLField(default="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png",
                             editable=False)
    main_pic = models.URLField(default="https://assets.pokemon.com/assets/cms2/img/pokedex/full/3.png",
                               editable=False)
    level = models.IntegerField(default=1)
    iv = models.IntegerField(default=0)

    # base stats
    b_hp = models.IntegerField('base hp', default=0, editable=False)
    b_defense = models.IntegerField('base defense', default=0, editable=False)
    b_attack = models.IntegerField('base attack', default=0, editable=False)
    b_s_defense = models.IntegerField(
        'base special defense', default=0, editable=False)
    b_s_attack = models.IntegerField(
        'base special attack', default=0, editable=False)
    b_speed = models.IntegerField('base speed', default=0, editable=False)

    # stats
    hp = models.IntegerField(default=0, editable=False)
    defense = models.IntegerField(default=0, editable=False)
    attack = models.IntegerField(default=0, editable=False)
    s_defense = models.IntegerField(
        'special defense', default=0, editable=False)
    s_attack = models.IntegerField('special attack', default=0, editable=False)
    speed = models.IntegerField(default=0, editable=False)

    # exp
    exp = models.IntegerField(default=0, editable=False)
    next_exp = models.IntegerField(default=0, editable=False)

    # def increase_exp(self, exp_inc):
    #     exp += exp_inc
    #     if(exp >= next_exp)
    #         next_exp =

    def calc_hp(self):
        return ((2 * self.b_hp + self.iv) * self.level) / 100 + self.level + 10

    def calc_stat(self, num):
        return ((2 * num + self.iv) * self.level) / 100 + 5

    def evolve(self):
        # check next evolution, update number and species
        self.number = 1
        self.species = 'charizard'
        # update base
        self.refresh_base()
        # update stats
        self.refresh_stats()

    def refresh_base(self):
        response = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{self.species}")
        p_stats = json.loads(response.content)['stats']
        self.b_hp = p_stats[0]['base_stat']
        self.b_attack = p_stats[1]['base_stat']
        self.b_defense = p_stats[2]['base_stat']
        self.b_s_attack = p_stats[3]['base_stat']
        self.b_s_defense = p_stats[4]['base_stat']
        self.b_speed = p_stats[5]['base_stat']

    def refresh_stats(self):
        self.hp = self.calc_hp()
        self.attack = self.calc_stat(self.b_attack)
        self.defense = self.calc_stat(self.b_defense)
        self.s_attack = self.calc_stat(self.b_s_attack)
        self.s_defense = self.calc_stat(self.b_s_defense)
        self.speed = self.calc_stat(self.b_speed)

    # occurs once, adds the correct picture, sprite, description, and pokemon number
    # (makes name = species if no name is specified)
    def add_meta(self):
        response = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{self.species}")
        temp = json.loads(response.content)
        self.sprite = temp['sprites']['front_default']
        self.number = str(temp['id'])
        pic_string = f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{self.number.zfill(3)}.png"
        self.main_pic = pic_string
        if self.name == "default name":
            self.name = self.species
        response2 = requests.get(
            f"https://pokeapi.co/api/v2/pokemon-species/{self.species}")
        temp2 = json.loads(response2.content)
        response3 = requests.get(temp2['evolution_chain']['url'])
        temp3 = json.loads(response3.content)
        self.set_evolutions(temp3)
        self.description = self.fix_string(
            temp2['flavor_text_entries'][6]['flavor_text'])

    def __str__(self):
        if self.name == self.species:
            return self.name
        return self.name + " (" + self.species + ")"

    @staticmethod
    def fix_string(string):
        result = string.replace("\f", " ")
        result = result.lower()
        result = result.capitalize()
        limit = len(result) - 3
        for x in range(0, limit):
            replace_index = x + 2
            if result[x] == '.':
                result = result[:replace_index] + \
                    result[replace_index].upper() + result[replace_index + 1:]
        return result

    def set_evolutions(self, evolution_chain):
        result = ['']
        chain = evolution_chain['chain']
        if len(chain['evolves_to']) != 0:
            # finds the second evolutions
            if chain['species']['name'] == self.species:
                for pokemon in chain['evolves_to']:
                    result.append(pokemon['species']['name'])
            # finds the third evolutions
            else:
                for pokemon in chain['evolves_to']:
                    if pokemon['species']['name'] == self.species:
                        for pokemon_2 in pokemon['evolves_to']:
                            result.append(pokemon_2['species']['name'])
        self.evolutions = result

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.refresh_base()
            self.refresh_stats()
            self.add_meta()
        super().save(*args, **kwargs)
