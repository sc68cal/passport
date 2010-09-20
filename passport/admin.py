# To change this template, choose Tools | Templates
# and open the template in the editor.

from django.contrib import admin
from passport.models import *
from django.shortcuts import redirect

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
	class Media:
		js = ('static/js/tiny_mce/tiny_mce.js',
          'js/textarea.js',)

class VenueAdmin(admin.ModelAdmin):
	exclude = ('lat','lng')
	class Media:
		js = ('static/js/tiny_mce/tiny_mce.js',
          'js/textarea.js',)


class ProfileAdmin(admin.ModelAdmin):
	search_fields = ['=lastname']
	
class ReservationAdmin(admin.ModelAdmin):
	search_fields = ['user__lastname']
	

admin.site.register(Venue, VenueAdmin)



admin.site.register(Event,EventAdmin)
admin.site.register(Ticket)
admin.site.register(Reservation,ReservationAdmin)
admin.site.register(DrexelProfile,ProfileAdmin)