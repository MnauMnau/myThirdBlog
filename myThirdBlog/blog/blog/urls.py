"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.contrib.sitemaps.views import sitemap # This need to be included because of sitemaps

from entries.sitemaps import EntrySitemap, AboutMeViewSitemap

from django.conf import settings
from django.conf.urls.static import static


# Here we add sitemaps for our webpage
sitemaps = {
    'entry-detail': EntrySitemap ,
    'static' : AboutMeViewSitemap ,
    #'products': ProductImageSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('sitemap.xml', sitemap, {'sitemaps' : sitemaps}), # new url for sitemaps
    path('',include('entries.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


