# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-14 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fips', '0010_auto_20170315_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(help_text='nickname of category name', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='ref_code',
            field=models.CharField(default='BOLi4AmyOx', max_length=10, verbose_name='Reference ID'),
        ),
    ]
