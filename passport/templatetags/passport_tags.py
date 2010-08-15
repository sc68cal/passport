'''
Created on Aug 8, 2010

@author: scollins
'''

from django import template
from passport.models import Event

register = template.Library()

def latest_events(parser,token):
    return LatestEventsNode()


class LatestEventsNode(template.Node):
    def render(self,context):
        print 'fired'
        context['latest_events'] = Event.objects.all().order_by('date')[:7]
        return ''
    
latest_events = register.tag(latest_events)