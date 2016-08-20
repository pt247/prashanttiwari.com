from django.contrib.syndication.views import Feed
from .models import Entry


class LatestPosts(Feed):
    title = "PT Blog"
    link = "/feed/"
    description = "Latest Posts of PT"

    def items(self):
        return Entry.objects.published()[:5]
