# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='address',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='organization',
            name='city',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='organization',
            name='zip_code',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
