from django.db import models
from django.forms import ModelForm
from pages.models import Page
from django.utils.translation import ugettext_lazy as _
from passport.models import Event,Venue

class Location(models.Model):

    event = models.ForeignKey(Event)

    # the foreign key _must_ be called page
    page = models.ForeignKey(Page)

class LocationForm(ModelForm):
    class Meta:
        model = Location

