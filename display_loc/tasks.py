from __future__ import absolute_import, unicode_literals
import requests
from .models import ISSLocation
from celery import task


@task()
def fill_db():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    loc = r.json()
    loc = loc['iss_position']
    iss_loc = ISSLocation(latitude=loc['latitude'], longitude=loc['longitude'])
    iss_loc.save()
