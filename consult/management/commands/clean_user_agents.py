
"""
Management command to remove bots/crawlers from trackers
"""

import math

from django.core.management.base import BaseCommand

from consult.models import Tracker
from consult.lib import search_crawler


class Command(BaseCommand):
    help = "Removes bots/crawlers from trackers"

    def handle(self, *args, **options):
        total_count = Tracker.objects.all().count()
        blocks = math.ceil(total_count/10000)
        
        for i in range(0, blocks):
            start = i*10000
            count = 0
            trackers = Tracker.objects.all()[start:10000]
            for tracker in trackers:
                if search_crawler.is_search_crawler(tracker.agent):
                    print("found: " + tracker.agent)
                    tracker.delete()
                    count += 1
            print("Deleted %d in range %d to %d" % (count, start, start+10000))
