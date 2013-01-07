from django.conf.urls import patterns, url
# just a test
urlpatterns = patterns('',
    url(r'^', 'setting.views.index'),
)