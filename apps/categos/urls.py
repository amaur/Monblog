from django.conf.urls import patterns, include, url
from .views import CategoryView

urlpatterns = patterns('apps.inicio.views',
    # Examples:
    # url(r'^$', 'Monblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^cate/$', CategoryView.as_view()),
)