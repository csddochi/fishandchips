# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-17 00:44
from __future__ import unicode_literals

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fips', '0013_auto_20170317_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='upload_file',
            field=models.FileField(upload_to='upload/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='ref_code',
            field=models.CharField(default='WgFca2dimS', max_length=10, verbose_name='Reference ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
