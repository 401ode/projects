import django_tables2 as tables
from .models import Project, FiscalYear
from django_tables2.utils import A
# from webfront.views import project

class ProjectsTable(tables.Table):
    name = tables.LinkColumn('webfront.views.project.ProjectView', args=[A('pk')])
    class Meta:
        model = Project
        fields = (
        'name',
        'client',
        'priority',
        'status',
        'start_fy',
        'completion_fy'
        )
        
        # exclude = (
        #     # 'name',
        #     'slug',
        #     'tagline',
        #     # 'client',
        #     'project_lead',
        #     'description',
        #     'impact',
        #     # 'status',
        #     # 'priority',
        #     'tech_effort',
        #     'agency_effort',
        #     'contractor_effort',
        #     # 'start_fy',
        #     # 'completion_fy',
        #     'blockers',
        #     'live_site_url',
        #     'github_url',
        #     'is_billable',
        #     'cloud_dot_gov',
        #     'rifans_number',
        #     'business_unit',
        #     'categories',
        # )