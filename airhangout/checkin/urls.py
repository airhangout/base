from django.conf.urls import patterns, url

#test

urlpatterns = patterns('',
    url(r'^', 'checkin.views.index'),
)