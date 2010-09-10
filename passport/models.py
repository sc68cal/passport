from django.db import models
import PIL

class Venue(models.Model):
	name = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=2)
	zip = models.CharField(max_length=5)
	about_text= models.TextField()
	student_perspectives_text = models.TextField()
	weekday_hours = models.CharField(max_length=255)
	weekend_hours = models.CharField(max_length=255,blank=True)
	phone = models.CharField(max_length=10)
	cost = models.CharField(max_length=255)
	url = models.CharField(max_length=1024)
	pic = models.ImageField(upload_to="venues",blank=True)

	def __unicode__(self):
		return self.name

	def apiaddr(self):
		return self.address.replace(" ","+") + "+" + self.city.replace(" ","+") + "+" + self.state + "+" + self.zip
	
	@models.permalink
	def get_absolute_url(self):
			return ('passport.views.venue_detail', [str(self.id)])

class Event(models.Model):
	venue = models.ForeignKey(Venue)
	date = models.DateTimeField()
	name = models.CharField(max_length=255)
	number_of_tickets = models.IntegerField()
	cost = models.CharField(max_length=255)
	pic = models.ImageField(upload_to='Events',blank=True)
	url = models.CharField(max_length=1024,blank=True)
	summary = models.TextField()

	def __unicode__(self):
		return self.name + " on " + str(self.date) + " at " + str(self.venue)
	
	@models.permalink
	def get_absolute_url(self):
			return ('passport.views.event_detail', [str(self.id)])

class DrexelProfile(models.Model):
	#http://blog.howiworkdaily.com/post/2008/jun/17/django-tutorial-abstract-base-classes-vs-model-inh/
	drexel_id = models.CharField(max_length=25)
	drexel_username = models.CharField(max_length=255)
	firstname = models.CharField(max_length=255)
	lastname = models.CharField(max_length=255)

	def __unicode__(self):
		return str(self.drexel_id)

class Ticket(models.Model):
	event = models.ForeignKey(Event)
	def __unicode__(self):
		return "Ticket #" + str(self.id) + " for " +  str(self.event) 

class Reservation(models.Model):
	ticket = models.ForeignKey(Ticket)
	user = models.ForeignKey(DrexelProfile)
	
	def __unicode__(self):
		return str(self.user) + " reservation for " + str(self.ticket)