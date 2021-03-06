# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-02 05:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_site', '0012_auto_20190202_0346'),
    ]

    operations = [
        migrations.CreateModel(
            name='upcomingtwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namefive', models.CharField(max_length=40, null=True, unique=True)),
                ('descriptionfive', models.CharField(max_length=100, null=True)),
                ('datefive', models.DateField(blank=True, null=True)),
                ('picturefive', models.ImageField(blank=True, null=True, upload_to='static')),
            ],
        ),
        migrations.DeleteModel(
            name='toprating',
        ),
        migrations.AlterField(
            model_name='movie',
            name='catagory',
            field=models.IntegerField(blank=True, choices=[(1, 'Bollywood'), (2, 'Hollywood'), (3, 'Tollywood'), (4, 'Toprating')], default=None, null=True),
        ),
    ]
