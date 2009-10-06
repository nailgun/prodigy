from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
	(r'^login/$', login),
	(r'^logout/$', logout),
	(r'^register/$', register),
	(r'^error/$', permission_error),
)

# vim:set ft=python ts=4 sw=4 tw=79 noet: 
