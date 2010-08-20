import authority
import settings
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
    (r'^article/', include('pages.urls')),
    (r'^$', include('passportsite.urls')),
)


if settings.DEBUG:
    urlpatterns += patterns('',    (r'', include('staticfiles.urls')),)