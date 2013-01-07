from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       
    url(r'^checkin/getFlightInfo/$', 'checkin.views.getFlightInfo'),                   
    url(r'^checkin/getFlightInfo/search/(?P<carrier>\w+)/(?P<flight>\d+)/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', 'checkin.views.getJson'),
    url(r'^checkin/getFlightInfo/findfriends/(?P<carrier>\w+)/(?P<flight>\d+)/$', 'checkin.views.findmyfriend'),
                       
)
