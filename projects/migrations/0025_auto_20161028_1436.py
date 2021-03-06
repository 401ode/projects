# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 18:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0024_auto_20161025_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(help_text='Contact First Name.', max_length=80)),
                ('last_name', models.CharField(help_text='Contact Last Name.', max_length=80)),
                ('title', models.CharField(help_text="Contact's Title", max_length=100)),
                ('email_address', models.EmailField(help_text="Contact's E-Mail address @ri.gov, unless an exception.", max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.AddField(
            model_name='businessunit',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='businessunit',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='category',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='client',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='fiscalyear',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fiscalyear',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='fundingsource',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fundingsource',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_id',
            field=models.IntegerField(default=0, help_text='The DoIT/ODE assigned Project ID.'),
        ),
        migrations.AlterField(
            model_name='client',
            name='omb_agency_code',
            field=models.CharField(blank=True, help_text='The OMB code id for the agency described here.', max_length=255, verbose_name='OMB Agency Code'),
        ),
        migrations.AlterField(
            model_name='fundingsource',
            name='funding_source_category',
            field=models.ForeignKey(help_text='The category (ITIF, Operational Budget, etc.of this funding source.', on_delete=django.db.models.deletion.CASCADE, to='projects.Category'),
        ),
        migrations.AlterField(
            model_name='project',
            name='blockers',
            field=models.TextField(blank=True, help_text='What stands in the way of this project?'),
        ),
    ]
