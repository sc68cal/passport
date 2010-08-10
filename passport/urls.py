# To change this template, choose Tools | Templates
# and open the template in the editor.

from django.conf.urls.defaults import patterns
from passport.models import Event,Venue
from passport.views import *


urlpatterns = patterns('',
	(r'^$',index_view),
	(r'^venue/(?P<object_id>\d+)/$', venue_detail),
	(r'^event/(?P<object_id>\d+)/$', event_detail),
	(r'^reserve/(?P<event_id>\d+)/$', reserve_ticket),
	(r'^venues/$',venue_list),
	(r'^calendar/json/',calendar_json),
	(r"^calendar/",event_calendar),

)