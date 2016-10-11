from django.conf.urls import url

from web.views.home import HomeView
from web.views.project import ProjectView
from web.views.fundingsource import FundingSourceView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^p/(?P<pk>[\w/\-]+)?$', ProjectView.as_view(), name='project'),
    url(r'^f/$', FundingSourceDetailView.as_view(), name='funding_sources'),
    url(r'^f/(?P<pk>[\w/\-]+)?$', FundingSourceDetailView.as_view(), name='funding_source'),
]
