from django.conf.urls import patterns, include, url
from django.contrib import admin
import timelinejs.urls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'timeline.views.home', name='home'),
    # url(r'^timeline/', include('timeline.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^timeline/', include(timelinejs.urls))
)
