# Generated by Django 3.0.8 on 2020-08-02 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='back_sprite',
            field=models.URLField(default='https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png', editable=False),
        ),
    ]
