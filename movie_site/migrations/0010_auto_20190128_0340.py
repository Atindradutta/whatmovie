# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-28 03:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_site', '0009_auto_20190126_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bollywoodone',
            old_name='nameone',
            new_name='name',
        ),
    ]
