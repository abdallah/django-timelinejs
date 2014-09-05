from django.conf.urls import *
from timelinejs.views import TimelineView

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', TimelineView.as_view(), name='timelineview'),
)
