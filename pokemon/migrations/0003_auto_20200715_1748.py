# Generated by Django 3.0.8 on 2020-07-15 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_pokemon'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.TextField(default='default', editable=False),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='iv',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]
