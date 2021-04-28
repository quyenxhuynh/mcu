# Generated by Django 3.1.7 on 2021-04-25 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcu_site', '0004_auto_20210425_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, through='mcu_site.CharacterPlayed', to='mcu_site.Actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='directors',
            field=models.ManyToManyField(blank=True, to='mcu_site.Director'),
        ),
    ]
