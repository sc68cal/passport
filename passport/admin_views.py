# To change this template, choose Tools | Templates
# and open the template in the editor.
from models import Event,Venue

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required


# http://www.ianlewis.org/en/reversing-django-admin-urls

@staff_member_required
def admin_create_event_tickets(request):
	return render_to_response('passport/admin/event.html',
		{'venue_list': Venue.objects.all()},
		RequestContext(request, {})
	)
