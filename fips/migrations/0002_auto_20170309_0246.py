# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-08 17:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fips', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='id',
            new_name='user_id',
        ),
    ]