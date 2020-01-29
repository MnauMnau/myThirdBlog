from django.contrib.sitemaps import Sitemap
from .models import Entry
from django.urls import reverse

# import imagesitemaps

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

''' 
class ImageSitemap(imagesitemaps.ImageSitemap):
    """ generic data for all ours image sitempas (use it as you used to with Django Sitemap) """  
    changefreq = 'weekly'
    priority = 0.5

    def lastmod(self, obj):
        return obj.modified

class ProductImageSitemap(ImageSitemap):
    """ a specific image sitemap for ours Product class """
    
    def items(self):
        """ Django Sitemap's items method """
        return Product.objects.all()

    def images(self, obj):
        """ this method allows you to define multiple images for an object """
        return obj.images()

    def image_loc(self, img):
        """ this required method define the image location """
        return img.doc.url

    def image_caption(self, img):
        """ this optional method define the image caption """
        return unicode(img)


    def location(self, obj):
       """ Django Sitemap's location method """
        return reverse(
            'webstore_product',
            kwargs={
                'slug_product': obj.slug,
            }
        )

 '''