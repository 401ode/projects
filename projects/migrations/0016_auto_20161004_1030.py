# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-04 14:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20160929_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='FiscalYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='FundingSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dollar_amount', models.PositiveIntegerField(default=0, help_text='The amount budgeted for this funding source.')),
                ('funding_status', models.PositiveIntegerField(choices=[(0, 'Proposed'), (1, 'Approved'), (2, 'Denied')], default=0, help_text='Overall approval status for this funding source.')),
            ],
        ),
        migrations.CreateModel(
            name='FundingSourceCategory',
            fields=[
                ('category_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projects.Category')),
            ],
            options={
                'verbose_name_plural': 'Funding Source Categories',
            },
            bases=('projects.category',),
        ),
        migrations.AlterModelOptions(
            name='businessunit',
            options={'verbose_name_plural': 'Business Units'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='project',
            name='agency_effort',
            field=models.PositiveIntegerField(default=0, help_text='Estimate of Agency staff necessary for the project.', verbose_name='Agency Staff Level of Effort'),
        ),
        migrations.AlterField(
            model_name='project',
            name='contractor_effort',
            field=models.PositiveIntegerField(default=0, help_text='Estimate of contractor staff necessary for the project.', verbose_name='Contractor Staff Level of Effort'),
        ),
        migrations.AlterField(
            model_name='project',
            name='rifans_number',
            field=models.CharField(blank=True, help_text='The unique identifier for the project inthe RIFANS financial system.', max_length=100, null=True, verbose_name='RIFANS Account Number'),
        ),
        migrations.AlterField(
            model_name='project',
            name='tech_effort',
            field=models.PositiveIntegerField(default=0, help_text='Estimate of technical staff necessary for the project.', verbose_name='Tech Staff Level of Effort'),
        ),
        migrations.AddField(
            model_name='fundingsource',
            name='funding_source_category',
            field=models.ForeignKey(help_text='The category (ITIF, Operational Budget, etc. of this funding source.', on_delete=django.db.models.deletion.CASCADE, to='projects.FundingSourceCategory'),
        ),
        migrations.AddField(
            model_name='fundingsource',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
        migrations.AlterUniqueTogether(
            name='fundingsource',
            unique_together=set([('project', 'funding_source_category')]),
        ),
    ]