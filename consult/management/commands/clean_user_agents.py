
"""
Management command to remove bots/crawlers from trackers
"""

from django.core.management.base import BaseCommand

from consult.models import Tracker
from consult.lib import search_crawler


class Command(BaseCommand):
    help = "Removes bots/crawlers from trackers"

    def handle(self, *args, **options):
        rts = Tracker.objects.all()[:100000]
        for rt in rts:
            if search_crawler.is_search_crawler(rt.agent):
                print("found: " + rt.agent)
                rt.delete()
