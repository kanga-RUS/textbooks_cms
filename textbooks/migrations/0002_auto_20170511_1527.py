# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-11 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textbooks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='slug',
        ),
        migrations.AlterField(
            model_name='textbook',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
