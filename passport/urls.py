# To change this template, choose Tools | Templates
# and open the template in the editor.

from django.conf.urls.defaults import patterns
from django.views.generic import list_detail
from passport.models import Event,Venue
from passport.views import *


urlpatterns = patterns('',
	(r'^events',list_detail.object_list,{"queryset": Event.objects.all()}),
	(r'^venues',list_detail.object_list,{"queryset": Venue.objects.all()}),
	(r'^venue/(?P<object_id>\d+)/$', venue_detail),

)