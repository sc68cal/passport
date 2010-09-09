# Create your views here.
from django.shortcuts import render_to_response
from pages.models import Page

def index_view(request):
    articles = Page.objects.filter(status=1,template='pages/passport/article.html').order_by('-publication_date')[:5]
    return render_to_response('passport/index.html',{'article_list':articles})
