from django.contrib import admin

from .models import Client, Project, BusinessUnit, Category
from .forms import ProjectForm, CategoryForm

admin.site.site_header = 'Project Dashboard Administration'

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('department', 'agency',)
    list_filter = ('department',)
    search_fields = ('department', 'agency',)


@admin.register(BusinessUnit)
class BusinessUnitAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    list_display = ('name', 'status', 'client')
    list_filter = ('status', 'is_billable', 'cloud_dot_gov', 'is_visible')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    # Only one field. Do we need a list_display or filter?
    # list_display = ('name')
