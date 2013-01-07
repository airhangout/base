from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       
    url(r'^getFlightInfo/$', 'checkin.views.getFlightInfo'),                   
    url(r'^getFlightInfo/search/(?P<carrier>\w+)/(?P<flight>\d+)/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', 'checkin.views.getJson'),
    url(r'^getFlightInfo/findfriends/(?P<carrier>\w+)/(?P<flight>\d+)/$', 'checkin.views.findmyfriend'),
                       
)
