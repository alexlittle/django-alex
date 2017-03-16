# oppia/reports/signals.py

from django.dispatch import Signal

from consult.models import Tracker

site_tracker = Signal(providing_args=["request", "data"])


def site_tracker_callback(sender, **kwargs):
    request = kwargs.get('request')
    data = kwargs.get('data')
    
    t = Tracker()
    t.url = request.build_absolute_uri()
    t.ip = request.META.get('REMOTE_ADDR','0.0.0.0')
    t.agent = request.META.get('HTTP_USER_AGENT','unknown')
    t.save()
    
    return


site_tracker.connect(site_tracker_callback)