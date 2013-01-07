from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'airhangout.views.home', name='home'),
    # url(r'^airhangout/', include('airhangout.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', include('login.urls')),
    url(r'^menu/', include('menu.urls')),
    url(r'^checkin/', include('checkin.urls')),
    url(r'^setting/', include('setting.urls')),
)
