# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 11:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0004_keywords'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Keywords',
            new_name='Keyword',
        ),
    ]
