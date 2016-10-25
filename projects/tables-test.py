import django_tables2 as tables
from django_tables2.utils import A
from .models import Project, FiscalYear

class ProjectsTable(tables.Table):
    name = tables.LinkColumn(ProjectView.as_view(),args=[A('pk')] )
    
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