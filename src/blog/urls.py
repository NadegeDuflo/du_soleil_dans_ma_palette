from django.urls import path

from blog.views import BlogPostDetail, BlogHome, PostDelete

app_name = 'blog'

urlpatterns = [
    path('', BlogHome.as_view(), name="home"),
    path('<str:slug>/', BlogPostDetail.as_view(), name='post'),
    path('<str:slug>/delete', PostDelete.as_view(), name='delete'),

]
