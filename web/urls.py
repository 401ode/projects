from django.conf.urls import url
from django.http import HttpRequest
from web.views.home import HomeView
from web.views.project import ProjectView, projects


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^p/(?P<pk>[\w/\-]+)?$', ProjectView.as_view(), name='project'),
    url(r'^list/$', projects, name='projects',)
]
