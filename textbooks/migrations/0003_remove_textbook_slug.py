# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-12 07:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textbooks', '0002_auto_20170511_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='textbook',
            name='slug',
        ),
    ]
