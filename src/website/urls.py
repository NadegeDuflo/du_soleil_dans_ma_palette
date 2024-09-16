from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from website.views import  home

urlpatterns = [
    path('admin_nadsun/', admin.site.urls, ),
    path('', home, name="home"),
    path('blog/', include('blog.urls')),
    path('gallery/', include('gallery.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('sendemail.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
