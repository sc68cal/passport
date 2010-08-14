
from django.conf.urls.defaults import patterns
from passportcms.views import *

urlpatterns = patterns('',
                       (r"^$", index_view)
)