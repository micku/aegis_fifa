from django.conf.urls import patterns, url

from tournaments import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<tournament_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<tournament_id>\d+)/calendar/$', views.calendar, name='calendar'),
)