# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-16 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='static')),
            ],
        ),
    ]
