from passport.models import *

tmp = Venue()

tmp.name = "Sean's House"
tmp.address = "4229 Baltimore Ave"
tmp.city = "Philadelphia"
tmp.state = "PA"
tmp.zip = '19104'
tmp.save()

tmp_event = Event()

tmp_event.name = "Test Event"
tmp.venue = tmp

tmp.save()
