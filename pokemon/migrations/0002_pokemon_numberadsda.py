# Generated by Django 3.0.8 on 2020-08-01 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='numberadsda',
            field=models.CharField(default=3, max_length=30),
        ),
    ]
