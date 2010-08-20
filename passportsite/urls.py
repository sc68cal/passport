# To change this template, choose Tools | Templates
# and open the template in the editor.

from django.conf.urls.defaults import patterns
from passport.models import Event,Venue
from passportsite.views import *


urlpatterns = patterns('',
    (r'^$',index_view),
)