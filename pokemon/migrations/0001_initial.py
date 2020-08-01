# Generated by Django 3.0.8 on 2020-08-01 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default name', max_length=30)),
                ('species', models.CharField(default='venusaur', max_length=30)),
                ('number', models.CharField(default=3, max_length=30)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('description', models.TextField(default='default')),
                ('sprite', models.URLField(default='https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png', editable=False)),
                ('main_pic', models.URLField(default='https://assets.pokemon.com/assets/cms2/img/pokedex/full/3.png', editable=False)),
                ('level', models.IntegerField(default=1)),
                ('iv', models.IntegerField(default=0)),
                ('b_hp', models.IntegerField(default=0, editable=False, verbose_name='base hp')),
                ('b_defense', models.IntegerField(default=0, editable=False, verbose_name='base defense')),
                ('b_attack', models.IntegerField(default=0, editable=False, verbose_name='base attack')),
                ('b_s_defense', models.IntegerField(default=0, editable=False, verbose_name='base special defense')),
                ('b_s_attack', models.IntegerField(default=0, editable=False, verbose_name='base special attack')),
                ('b_speed', models.IntegerField(default=0, editable=False, verbose_name='base speed')),
                ('hp', models.IntegerField(default=0, editable=False)),
                ('defense', models.IntegerField(default=0, editable=False)),
                ('attack', models.IntegerField(default=0, editable=False)),
                ('s_defense', models.IntegerField(default=0, editable=False, verbose_name='special defense')),
                ('s_attack', models.IntegerField(default=0, editable=False, verbose_name='special attack')),
                ('speed', models.IntegerField(default=0, editable=False)),
                ('exp', models.IntegerField(default=0, editable=False)),
                ('next_exp', models.IntegerField(default=0, editable=False)),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
