# To change this template, choose Tools | Templates
# and open the template in the editor.

from django.db import models
from django.contrib import admin
from passport.models import *

class EventAdmin(admin.ModelAdmin):
	actions = ['create_tickets','delete_tickets']
	def create_tickets(self,request,queryset):
		count = 0
		for event in queryset:
			if len(event.ticket_set.all()) < event.number_of_tickets:
				for i in range(0,event.number_of_tickets):
					a = Ticket()
					a.event = event
					a.save()
					count += 1
		self.message_user(request, "%s tickets successfully created" % count)




admin.site.register(Venue)
admin.site.register(Event,EventAdmin)
admin.site.register(Ticket)
admin.site.register(Reservation)