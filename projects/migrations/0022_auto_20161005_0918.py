# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-05 13:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_auto_20161004_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundingsource',
            name='funding_source_category',
            field=models.ForeignKey(help_text='The category (ITIF, Operational Budget, etc. of this funding source.', on_delete=django.db.models.deletion.CASCADE, to='projects.Category'),
        ),
    ]
