# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-28 03:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_site', '0010_auto_20190128_0340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bollywoodone',
            old_name='name',
            new_name='nameone',
        ),
    ]
