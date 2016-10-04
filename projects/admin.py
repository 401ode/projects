from django.contrib import admin

from .models import (
    Client, 
    Project, 
    BusinessUnit, 
    Category, 
    FundingSource,
    FundingSourceCategory,
    FiscalYear
    )
from .forms import ProjectForm, CategoryForm

admin.site.site_header = 'Project Dashboard Administration'

class FundingSourceInline(admin.TabularInline):
    model = FundingSource
    extra = 3


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
    inlines = [FundingSourceInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    # Only one field. Do we need a list_display or filter?
    # list_display = ('name')
    list_display = ('name', 'category_type')
    list_filter = ('name','category_type')


@admin.register(FiscalYear)
class FiscalYearAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    
@admin.register(FundingSource)
class FundingSourceAdmin(admin.ModelAdmin):
    """
    For maintaining Funding Sources.
    
    """
    def get_project_client(self):
        """
        Return the client that the project's funding source is for. 
        """
        return self.project.client_set.first()
    # project_client.admin_order_field = "project__client"
    list_display = ('project', 'fiscal_year', 'funding_source_category', 'dollar_amount_display', 'funding_status')
    list_filter = ('project', 'funding_source_category', 'funding_status')