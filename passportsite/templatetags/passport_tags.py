'''
Created on Aug 8, 2010

@author: scollins
'''

from django import template
from passport.models import Event
from pages.models import Page

register = template.Library()

def latest_events(parser,token):
    return LatestEventsNode()


class LatestEventsNode(template.Node):
    def render(self,context):
        print 'fired'
        context['latest_events'] = Event.objects.all().order_by('date')[:7]
        return ''
    
latest_events = register.tag(latest_events)


def latest_per_category(parser,token):
    return LatestArticleNode()

class LatestArticleNode(template.Node):
    def render(self,context):
        context['latest_articles'] = Page.objects.filter(status=1).filter(template='pages/passport/article.html').order_by('publication_date')[:7]
        return ''

latest_per_category = register.tag(latest_per_category)