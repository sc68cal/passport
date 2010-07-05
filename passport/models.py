from django.db import models
import Image
from django.contrib.auth.models import User, UserManager



class Venue(models.Model):
	name = models.CharField(max_length=255)
	google_map_url = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	hours = models.CharField(max_length=255)
	#phone = models.PhoneNumberField()
	#img = models.ImageField(upload_to="venues")

	def __unicode__(self):
		return self.name




# Create your models here.
class Event(models.Model):
	venue = models.ForeignKey(Venue)
	date = models.DateTimeField()
	name = models.CharField(max_length=255)
	number_of_tickets = models.IntegerField()

	def __unicode__(self):
		return self.name + " on " + str(self.date) + " at " + str(self.venue)

class UserProfile(models.Model):
	#http://blog.howiworkdaily.com/post/2008/jun/17/django-tutorial-abstract-base-classes-vs-model-inh/
	user =  models.ForeignKey(User,unique=True)

	def __unicode__(self):
		return str(self.user)

class Ticket(models.Model):
	event = models.ForeignKey(Event)
	def __unicode__(self):
		return str(self.event)

class Reservation(models.Model):
	ticket = models.ForeignKey(Ticket)
	user = models.ForeignKey(UserProfile)