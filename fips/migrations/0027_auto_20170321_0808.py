# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-20 23:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fips', '0026_auto_20170321_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ref_code',
            field=models.CharField(default='AURF6Pi7NZ', max_length=10, verbose_name='Reference ID'),
        ),
    ]
