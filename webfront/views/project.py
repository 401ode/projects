from django.views.generic.detail import DetailView
from django.shortcuts import render
from projects.models import Project
from projects.tables import ProjectsTable


class ProjectView(DetailView):
    context_object_name = 'project'
    model = Project
    template_name = 'web/project.html'

def projects(request):
    table = ProjectsTable(Project.objects.all())
    return render(request, 'web/project_list.html', {'projects': table})