# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textbooks', '0003_remove_textbook_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textbook',
            name='image',
            field=models.ImageField(blank=True, default='media/book.jpg', null=True, upload_to=''),
        ),
    ]