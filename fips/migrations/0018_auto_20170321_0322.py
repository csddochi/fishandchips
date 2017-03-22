# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-20 18:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fips', '0017_auto_20170318_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_comments', to='fips.Post')),
            ],
            options={
                'verbose_name_plural': 'Comments',
                'ordering': ['-created_date'],
            },
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_date'], 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterField(
            model_name='user',
            name='ref_code',
            field=models.CharField(default='134TSvAZkZ', max_length=10, verbose_name='Reference ID'),
        ),
    ]