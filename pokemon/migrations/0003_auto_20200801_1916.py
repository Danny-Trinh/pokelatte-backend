# Generated by Django 3.0.8 on 2020-08-02 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_pokemon_back_sprite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='next_exp',
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='exp',
            field=models.IntegerField(default=0),
        ),
    ]