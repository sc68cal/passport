import authority

from django.conf.urls.defaults import url, include, patterns
from django.conf.urls.defaults import handler404, handler500
from django.contrib import admin

from pages.views import details

admin.autodiscover()
authority.autodiscover()

urlpatterns = patterns('',
    (r'^authority/', include('authority.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^passport/', include('passport.urls')),
    (r'^admin/', include(admin.site.urls)),
    # Trick for Django to support static files
    # (security hole: only for Dev environement! remove this on Prod!!!)
    (r'', include('staticfiles.urls')),


    
    (r'^', include('pages.urls')),
    
    # make tests fail if a backend is not present on the system
    (r'^search/', include('haystack.urls')),
)


