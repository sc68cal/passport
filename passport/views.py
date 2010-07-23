# Create your views here.
from django.views.generic import list_detail
from django.shortcuts import get_object_or_404
from passport.models import Venue, Event,Ticket

def venue_detail(request, object_id):
	venue = get_object_or_404(Venue, pk=object_id)

	# Show the detail page
	return list_detail.object_detail(
		request,
		queryset = Venue.objects.all(),
		object_id = object_id,
		extra_context={"title":"Drexel Passport: "+str(venue)}

	)

def event_detail(request, object_id):
	event = get_object_or_404(Event, pk=object_id)

	# Show the detail page
	return list_detail.object_detail(
		request,
		queryset = Event.objects.all(),
		object_id = object_id,
		template_object_name = "event",
		extra_context={"title":"Drexel Passport: "+str(event)}
	)


def reserve_ticket(request, event_id):
	event = get_object_or_404(Event, pk=event_id)

	# See if any tickets are available
	#http://docs.djangoproject.com/en/dev/topics/db/queries/#spanning-multi-valued-relationships
	results = Ticket.objects.filter(event=event.id).filter(reservation__user__isnull=True)
	if results:
		print "Tickets available"
	else:
		print "Tickets not available"

