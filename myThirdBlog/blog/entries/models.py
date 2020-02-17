from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Entry(models.Model):
    entry_title = models.CharField(max_length = 50)
    entry_text = models.TextField()
    entry_date = models.DateTimeField(auto_now_add = True)
    entry_author = models.ForeignKey(User, on_delete = models.CASCADE)
    entry_nViews = models.IntegerField(default = 0) # This will count how many times someone click on page
    entry_category = models.ForeignKey('Category', null=True, blank=True, on_delete = models.CASCADE)

    def inceraseNViews(self,entry_nViews):
        entry_nViews = entry_nViews + 1

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f'{self.entry_title}'

    def get_absolute_url(self): # This is some method for creation static map
        kwargs = {"pk": str(self.pk), "random": slugify(self.entry_title)}
        #kwargs = {"pk" :str(self.pk), "slug" : self.entry_title}
        #return reverse('entry-detail',args = [str(self.pk)])
        return reverse('entry-detail',kwargs = kwargs)


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    class Meta:
        #enforcing that there can not be two categories under a parent with same slug
        # __str__ method elaborated later in post.  use __unicode__ in place of
        # __str__ if you are using python 2
 
        verbose_name_plural = "categories"     

    def __str__(self):                           
        full_path = [self.name]                  
        return f'{self.name}'
