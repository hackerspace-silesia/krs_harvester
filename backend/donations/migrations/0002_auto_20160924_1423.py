# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 14:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='donator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donations', to='donations.Donator'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donations', to='organizations.Organization'),
        ),
    ]
