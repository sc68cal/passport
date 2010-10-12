'''
Created on Aug 8, 2010

@author: scollins
'''

from django import template
from passport.models import Event
from pages.models import Page
from news.models import NewsLink
from datetime import datetime

register = template.Library()

def latest_events(parser,token):
    return LatestEventsNode()


class LatestEventsNode(template.Node):
    def render(self,context):
        context['latest_events'] = Event.objects.filter(date__gt=datetime.now()).order_by('date')[:7]
        return ''
    
latest_events = register.tag(latest_events)


def latest_per_category(parser,token):
    return LatestArticleNode()

class LatestArticleNode(template.Node):
    def render(self,context):
        context['latest_articles'] = Page.objects.filter(status=1).filter(template='pages/passport/article.html').order_by('-publication_date')[:7]
        return ''

latest_per_category = register.tag(latest_per_category)

def news_links(parser,token):
    return NewsLinkNode()

class NewsLinkNode(template.Node):
    def render(self,context):
        context['news_links'] = NewsLink.objects.all()
        return ''
        
news_links = register.tag(news_links)


def replace_spaces(value):
    return value.replace(' ',"_")

register.filter('replace_spaces', replace_spaces)
    