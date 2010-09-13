# Create your views here.
from django.http import HttpResponse
from django.db import transaction
import json
from django.views.generic import list_detail
from django.shortcuts import get_object_or_404, render_to_response
from passport.models import Venue, Event,Ticket,Reservation,DrexelProfile
from datetime import datetime
from passport.forms import DrexelIDForm,UploadForm
from django.contrib.auth.decorators import login_required


def venue_list(request):
	return list_detail.object_list(request, Venue.objects.all().order_by('name'))

def event_list(request):
	return list_detail.object_list(request, Event.objects.all().order_by('date'))

def venue_detail(request, object_id):
	get_object_or_404(Venue, pk=object_id)

	# Show the detail page
	return list_detail.object_detail(
		request,
		queryset = Venue.objects.all(),
		object_id = object_id,
	)
def event_detail(request, object_id):
	get_object_or_404(Event, pk=object_id)

	# Show the detail page
	return list_detail.object_detail(
		request,
		queryset = Event.objects.all(),
		object_id = object_id,
		template_object_name = "event",
	)

def reservation_detail(request,object_id):
	return list_detail.object_detail(
										request,
										queryset = Reservation.objects.all(),
										object_id = object_id,
									)
	
@transaction.commit_on_success
def reserve_ticket(request, event_id):
	event = get_object_or_404(Event, pk=event_id)
	form = DrexelIDForm()
	# See if any tickets are available
	#http://docs.djangoproject.com/en/dev/topics/db/queries/#spanning-multi-valued-relationships
	results = Ticket.objects.filter(event=event.id).filter(reservation__user__isnull=True)
	if request.method == 'POST' and results.count():
		form = DrexelIDForm(request.POST)
		if form.is_valid():
			reservation = Reservation()
			drexel_user = DrexelProfile.objects.filter(drexel_id__exact=form.cleaned_data['drexel_id'],
													drexel_username__exact=form.cleaned_data['drexel_username'])
			if not drexel_user.count():
				return render_to_response('passport/reservation.html',{'ticket':results[0],"form":form,'msg': "Invalid Login"})
			reservation.ticket = results[0]
			reservation.user = drexel_user[0]
			reservation.save()
			return reservation_detail(request,reservation.id)
		else:
			return render_to_response('passport/reservation.html',{'ticket':results[0],"form":form})
	elif results.count():
		#print "Tickets available"
		return render_to_response('passport/reservation.html',{'ticket':results[0],"form":form})
	else:
		return render_to_response('passport/tickets_unavailable.html')
	
@login_required
def profile_upload(request):
	form = UploadForm(request.POST,request.FILES)
	
	if request.method == "POST":
		if form.is_valid():
			print form
		else:
			return render_to_response('passport/profile_upload.html',{'form':form})
	else:
		return render_to_response('passport/profile_upload.html',{'form':form})
		
		

def event_calendar(request):
	return render_to_response('passport/calendar.html')

def map(request):
	return render_to_response('passport/map.html')

def calendar_json(request):
	if request.GET and request.is_ajax():
		data = []
		start_date = datetime.fromtimestamp(float(request.GET.get('start')))
		end_date = datetime.fromtimestamp(float(request.GET.get('end')))
		events = Event.objects.filter(date__gte=start_date).filter(date__lte=end_date)
		
		for event in events:
			data.append({"id":event.id,"title":event.name,"start":str(event.date),"url":event.get_absolute_url()})
		
		return HttpResponse(json.dumps(data))
	else:
		return HttpResponse("A start date and end date is required in your request.")
	
def map_json(request):
	data = []
	for venue in Venue.objects.all():
		data.append([venue.apiaddr(),venue.name,venue.infobox()])
	return HttpResponse(json.dumps(data))