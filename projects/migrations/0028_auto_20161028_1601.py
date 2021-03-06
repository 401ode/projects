# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0027_auto_20161028_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='admin_only',
            field=models.BooleanField(default=False, help_text='This note has been flagged to be visible only to adminstrators.'),
        ),
        migrations.AddField(
            model_name='note',
            name='archived',
            field=models.BooleanField(default=False, help_text='This note has been archived. Or not.'),
        ),
    ]
