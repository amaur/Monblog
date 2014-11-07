from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Monblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('apps.inicio.urls')),
    url(r'^artigo/', include('apps.artigos.urls')),
    url(r'^cat/', include('apps.categos.urls')),
    url(r'^comentaire/', include('apps.commentaire.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
