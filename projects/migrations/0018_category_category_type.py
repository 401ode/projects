# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-04 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0024_auto_20161005_1105'),
        ('projects', '0017_auto_20161004_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_type',
            field=models.CharField(default='Project', max_length=20),
        ),
    ]
