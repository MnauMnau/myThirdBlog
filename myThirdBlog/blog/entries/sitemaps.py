from django.contrib.sitemaps import Sitemap
from .models import Entry
from django.urls import reverse

class EntrySitemap(Sitemap):

    def items(self):
        return Entry.objects.all()


# By this we will create static map to basic pages
class AboutMeViewSitemap(Sitemap):


    def items(self): # Firstly itme where are show all items
        return ['about_me',
                'blog-home']

    def location(self,item):
        return reverse(item)