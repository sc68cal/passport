# To change this template, choose Tools | Templates
# and open the template in the editor.

from django.conf.urls.defaults import patterns
from django.views.generic import list_detail
from passport.models import Event,Venue
from passport.views import *


urlpatterns = patterns('',
	(r'^venue/(?P<object_id>\d+)/$', venue_detail),
	(r'^event/(?P<object_id>\d+)/$', event_detail),
	(r'^reserve/(?P<event_id>\d+)/$', reserve_ticket),
	(r'^all/',list_detail.object_list,{"queryset": Venue.objects.all()}),
	(r'^events/',list_detail.object_list,{"queryset": Event.objects.all()}),
	(r"^calendar/",event_calendar),

)