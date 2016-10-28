"""
Pretty standard collection of objects being added to
Django administration screens.

This is all to allow proper sysadmins to maintain data.
Next steps are to allow ability to inline edit from front-end.
"""


from django.contrib import admin

from .models import (
    Client,
    Project,
    BusinessUnit,
    Category,
    FundingSource,
    FiscalYear,
    Contact,
    Blocker,
    Note
    )
from .forms import ProjectForm, CategoryForm

admin.site.site_header = 'RIODE Project Dashboard Administration'

class FundingSourceInline(admin.TabularInline):
    """
    Present inline editing ability for Funding Sources.
    """
    model = FundingSource
    extra = 3

class BlockerInline(admin.TabularInline):
    """
    Present inline editing ability for Blockers.
    """
    model = Blocker
    extra = 2
    
class NoteInline(admin.TabularInline):
    """
    Present inline editing ability for Notes.
    """
    model = Note
    extra = 2

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """
    For Maintaining Clients.
    """
    list_display = ('department', 'agency',)
    list_filter = ('department',)
    search_fields = ('department', 'agency',)


@admin.register(BusinessUnit)
class BusinessUnitAdmin(admin.ModelAdmin):
    """
    For maintaining Busines Units.
    """
    list_display = ('name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    For maintaining Projects. Includes the FundingSourceInline,
    BlockerInline, NoteInline editing tools.
    """
    form = ProjectForm
    list_display = ('name', 'status', 'client')
    list_filter = ('status', 'is_billable', 'cloud_dot_gov', 'is_visible')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    inlines = [FundingSourceInline,
               BlockerInline,
               NoteInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    For maintaining Categories.
    """
    form = CategoryForm
    # Only one field. Do we need a list_display or filter?
    # list_display = ('name')
    list_display = ('name', 'category_type')
    list_filter = ('name', 'category_type')


@admin.register(FiscalYear)
class FiscalYearAdmin(admin.ModelAdmin):
    """
    For maintaining Fiscal Years.
    """
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
    list_display = ('project',
                    'fiscal_year',
                    'funding_source_category',
                    'dollar_amount',
                    'funding_status')
    list_filter = ('project',
                   'funding_source_category',
                   'funding_status')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    For maintaining project contacts.
    """
    list_display = ('first_name',
                    'last_name',
                    'title',
                    'email_address')
    list_filter = ('first_name',
                   'last_name',
                   'title',
                   'email_address')
