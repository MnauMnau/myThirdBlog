from django.urls import path

from .views import HomeView, EntryView, CreateEntryView, AboutMeView
from django.contrib.sitemaps.views import sitemap # This need to be included because of sitemaps
from django.views.generic import TemplateView

from .sitemaps import EntrySitemap

from django.conf import settings
from django.conf.urls.static import static


# Here we add sitemaps for our webpage

sitemaps = {
    'entry-detail': EntrySitemap
}

urlpatterns = [
    path('', HomeView.as_view(), name = 'blog-home'),
    path('sitemap.xml', sitemap, {'sitemaps' : sitemaps}), # new url for sitemaps
    path('entry/<int:pk>-<str:random>/',EntryView.as_view(), name = 'entry-detail' ),
    path('create_entry',CreateEntryView.as_view(success_url = '/'), name = 'create_entry'),
    path('about_me',AboutMeView.as_view() ,name = 'about_me'),
    path('image-sitemap.xml',TemplateView.as_view(template_name='entries/image-sitemap.xml', content_type='text/xml'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)