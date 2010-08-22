# To change this template, choose Tools | Templates
# and open the template in the editor.

from django.conf.urls.defaults import patterns
from passport.models import Event,Venue
from passport.views import *


urlpatterns = patterns('',
	(r'^venue/(?P<object_id>\d+)/$', venue_detail),
	(r'^event/(?P<object_id>\d+)/$', event_detail),
	(r'^reserve/(?P<event_id>\d+)/$', reserve_ticket),
	(r'^venues/$',venue_list),
	(r'^events/$',event_list),
	(r"^calendar/",event_calendar),
	(r'^map/',map),
	(r'^api/calendar/json/',calendar_json),
	(r'^api/map/json/',map_json),
)