from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    #url(r'^', 'login.views.index'),
	(r'^register/$', views.register),
	(r'^loginResult/$', views.loginResult),
	(r'^login/$', views.login),
	#(r'^registerResult/$', login.views.registerResult),
	(r'^testResult/$',views.testSession),
)