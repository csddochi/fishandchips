# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-20 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fips', '0023_auto_20170321_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ref_code',
            field=models.CharField(default='kZhMUsr5er', max_length=10, verbose_name='Reference ID'),
        ),
    ]
