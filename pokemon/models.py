from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import pokebase as poke

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
    evolve_chain = models.IntegerField(default=0, editable=False)
    gender = models.CharField(
        choices=GENDER, max_length=1, default='M')

    # meta, will change
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
    prev_exp = models.IntegerField(default=0, editable=False)
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
        p_stats = poke.pokemon(self.species).stats
        self.b_hp = p_stats[0].base_stat
        self.b_defense = p_stats[1].base_stat
        self.b_attack = p_stats[2].base_stat
        self.b_s_attack = p_stats[3].base_stat
        self.b_s_defense = p_stats[4].base_stat
        self.b_speed = p_stats[5].base_stat

    def refresh_stats(self):
        self.hp = self.calc_hp()
        self.defense = self.calc_stat(self.b_defense)
        self.attack = self.calc_stat(self.b_attack)
        self.s_attack = self.calc_stat(self.b_s_attack)
        self.s_defense = self.calc_stat(self.b_s_defense)
        self.speed = self.calc_stat(self.b_speed)

    # occurs once, adds the correct picture, sprite, and pokemon number
    def add_meta(self):
        temp = poke.pokemon(self.species)
        self.sprite = temp.sprites.front_default
        self.number = str(temp.order)
        pic_string = f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{self.number.zfill(3)}.png"
        self.main_pic = pic_string
        temp2 = poke.pokemon_species(self.species)
        self.evolve_chain = temp2.evolution_chain.id
        print(f"pic: {self.sprite}")
        print(f"evolve num: {self.evolve_chain}")
        print(f"evolve num: {self.main_pic}")

    def __str__(self):
        return self.name + " (" + self.species + ")"

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.refresh_base()
            self.refresh_stats()
            self.add_meta()
        super().save(*args, **kwargs)
