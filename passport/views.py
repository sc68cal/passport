# Create your views here.
from django.views.generic import list_detail
from django.shortcuts import get_object_or_404
from passport.models import Venue

def venue_detail(request, object_id):
    # Look up the Author (and raise a 404 if she's not found)
    venue = get_object_or_404(Venue, pk=object_id)

    # Show the detail page
    return list_detail.object_detail(
        request,
        queryset = Venue.objects.all(),
        object_id = object_id
    )
