# Generated by Django 3.1.4 on 2021-04-09 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcu_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', editable=False, max_length=255)),
                ('password', models.CharField(default='', editable=False, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MovieDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', editable=False, max_length=255)),
                ('director', models.CharField(default='', editable=False, max_length=255)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]
