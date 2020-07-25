# Generated by Django 3.0.8 on 2020-07-24 04:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pokemon', '0004_auto_20200721_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
