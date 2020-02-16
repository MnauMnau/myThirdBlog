from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Entry, Category

class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Entry,SomeModelAdmin)

admin.site.register(Category) # To add new possibility to add category