# Create your views here.
from django.http import HttpResponse
import json
from django.views.generic import list_detail
from django.shortcuts import get_object_or_404, render_to_response
from passport.models import Venue, Event,Ticket
from datetime import datetime

def index_view(request):
	return render_to_response('passport/base.html')

def venue_list(request):
	return list_detail.object_list(request, Venue.objects.all())

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

def event_calendar(request):
	
	return render_to_response('passport/calendar.html')

def calendar_json(request):
	if request.GET:
		data = []
		start_date = datetime.fromtimestamp(float(request.GET.get('start')))
		end_date = datetime.fromtimestamp(float(request.GET.get('end')))
		events = Event.objects.filter(date__gte=start_date).filter(date__lte=end_date)
		
		for event in events:
			data.append({"id":event.id,"title":event.name,"start":str(event.date),"url":event.get_absolute_url()})
		
		return HttpResponse(json.dumps(data))
	else:
		return HttpResponse("A start date and end date is required in your request.")
	