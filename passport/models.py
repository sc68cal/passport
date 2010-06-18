from django.db import models


class Venue(Models.model):
	name = models.CharField()
	google_map_url = models.CharField()
	description = models.CharField()
	hours = models.Charfield()
	phone = models.PhoneNumberField()
	img = models.ImageField()




# Create your models here.
class Event(Models.model):
	venue = models.ForeignKey(Venue)
	date = models.DateTimeField()
