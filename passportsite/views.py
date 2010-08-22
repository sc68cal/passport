# Create your views here.
from django.shortcuts import render_to_response
from pages.models import Page

def index_view(request):
    articles = []
    for pg in Page.objects.filter(status=1):
            if not pg.is_child_node() and pg.get_children():
                articles.append(pg.get_date_ordered_children_for_frontend()[0])
    print articles
    return render_to_response('passport/index.html',{'article_list':articles})
