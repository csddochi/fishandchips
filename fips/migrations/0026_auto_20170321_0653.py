# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-20 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fips', '0025_auto_20170321_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ref_code',
            field=models.CharField(default='PbR04GFR0J', max_length=10, verbose_name='Reference ID'),
        ),
    ]
