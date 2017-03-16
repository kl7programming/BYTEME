# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 00:39
from __future__ import unicode_literals

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
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Save',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('attack', models.IntegerField(max_length=3)),
                ('defence', models.IntegerField(max_length=3)),
                ('speed', models.IntegerField(max_length=3)),
                ('health', models.IntegerField(max_length=3)),
                ('total_health', models.IntegerField(max_length=3)),
                ('next_level', models.IntegerField(max_length=1)),
                ('time', models.TimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='leaderboard',
            name='save',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='KittyKrawler.Save'),
        ),
        migrations.AddField(
            model_name='leaderboard',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='item',
            name='save_item',
            field=models.ManyToManyField(to='KittyKrawler.Save'),
        ),
    ]
