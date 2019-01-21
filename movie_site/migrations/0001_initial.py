# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-16 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, null=True, unique=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('duration', models.DurationField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='static')),
                ('Path', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
