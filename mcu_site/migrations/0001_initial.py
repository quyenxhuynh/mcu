# Generated by Django 3.1.4 on 2021-05-01 04:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterPlayed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_name', models.CharField(max_length=32)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mcu_site.actor')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('title', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('synopsis', models.CharField(max_length=2048)),
                ('year', models.CharField(max_length=10)),
                ('runtime', models.CharField(max_length=32)),
                ('actors', models.ManyToManyField(blank=True, through='mcu_site.CharacterPlayed', to='mcu_site.Actor')),
                ('directors', models.ManyToManyField(blank=True, to='mcu_site.Director')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField()),
                ('date_written', models.DateTimeField(auto_now_add=True)),
                ('review_text', models.TextField(max_length=2048)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mcu_site.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='director',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mcu_site.person'),
        ),
        migrations.AddField(
            model_name='characterplayed',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mcu_site.movie'),
        ),
        migrations.AddField(
            model_name='actor',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mcu_site.person'),
        ),
    ]
