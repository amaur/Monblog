from django.conf.urls import patterns, include, url
from .views import Index, my_page ,art_likes

urlpatterns = patterns('apps.inicio.views',
    # Examples:
    # url(r'^$', 'Monblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index/$', Index),
    url(r'^Zinli/$', my_page),
    url(r'^art_likes/$', art_likes),
    
)