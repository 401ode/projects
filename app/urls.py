from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^', include(('webfront.urls', 'webfront'), namespace='webfront')),
    url(r'^', include(('projects.urls', 'projects'), namespace='projects')),
    url(r'^admin/', admin.site.urls),
]
