# Create your views here.
from django.shortcuts import render_to_response

def index_view(request):
    return render_to_response('passport/index.html')
