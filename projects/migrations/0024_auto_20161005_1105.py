# -*- coding: utf-8 -*-
"""
Manual migration to compensate for changing `category_type` of 
'Category' model from str to int. 
"""
# Generated by Django 1.9.6 on 2016-10-05 15:05
from __future__ import unicode_literals

from django.apps import apps
from django.db import connection, migrations
# from projects.models import Category

def update_category_from_str_to_int(apps=apps, schema_editor=connection.schema_editor()):
    """
    Get categories model from django app. 
    Get db_alias from connection schema editor.Get
    Get all Category objects. 
    If category_type for any category == "Project",
    then make it int(0). 
    Save all categories. 
    """
    
    Category = apps.get_model("projects", "Category")
    db_alias = schema_editor.connection.alias
    categories = Category.objects.using(db_alias).all()
    for category in categories:
        if category.category_type == "Project":
            category.category_type = int(0)
            category.save()
    


class Migration(migrations.Migration):

    dependencies = [
        # ('projects', '0023_auto_20161005_1025'),
        ('projects', '0018_category_category_type'),
    ]

    operations = [
        migrations.RunPython(update_category_from_str_to_int),
    ]
