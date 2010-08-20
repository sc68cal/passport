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
        context['latest_articles'] = []
        for pg in Page.objects.all():
            if not pg.is_child_node() and not pg.is_leaf_node():
                context['latest_articles'].append(pg.get_date_ordered_children_for_frontend()[0])
        return ''

latest_per_category = register.tag(latest_per_category)