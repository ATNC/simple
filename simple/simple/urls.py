from django.conf.urls import patterns, include, url
from django.contrib import admin
from data.views import show_next, processed

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simple.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', show_next),
    url(r'^(?P<id>\d+)', processed),
)
