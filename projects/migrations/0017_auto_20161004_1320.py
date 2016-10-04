# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-04 17:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_auto_20161004_1030'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fiscalyear',
            options={'verbose_name_plural': 'Fiscal Years'},
        ),
        migrations.AlterModelOptions(
            name='fundingsource',
            options={'verbose_name_plural': 'Funding Sources'},
        ),
        migrations.AddField(
            model_name='fundingsource',
            name='fiscal_year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.FiscalYear'),
        ),
        migrations.AlterUniqueTogether(
            name='fundingsource',
            unique_together=set([('project', 'funding_source_category', 'fiscal_year')]),
        ),
    ]
