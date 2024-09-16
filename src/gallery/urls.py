from django.urls import path

from gallery.views import GalleryDelete, GalleryHome, GalleryDetail

app_name = 'gallery'


urlpatterns = [
    path('', GalleryHome.as_view(), name="home"),
    path('<str:slug>/', GalleryDetail.as_view(), name='detail'),
    path('<str:slug>/delete', GalleryDelete.as_view(), name='delete'),

]