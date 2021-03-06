# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-16 21:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fips', '0012_auto_20170317_0139'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('upload_file', models.FileField(upload_to=b'upload/')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('hits', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-created_date'],
                'verbose_name_plural': 'Upload Files',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='ref_code',
            field=models.CharField(default='gum3Fq8AXX', max_length=10, verbose_name=b'Reference ID'),
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fips.Category'),
        ),
    ]
