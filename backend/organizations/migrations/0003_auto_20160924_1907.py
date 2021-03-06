# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 19:07
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_auto_20160924_1423'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='address',
            new_name='street',
        ),
        migrations.AddField(
            model_name='organization',
            name='aim',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='gmina',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='powiat',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='wojewodztwo',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='organization',
            name='krs',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=8, null=True),
        ),
    ]
