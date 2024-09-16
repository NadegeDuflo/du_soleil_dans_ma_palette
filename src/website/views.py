from django.shortcuts import render

from blog.models import BlogPost
from gallery.models import Gallery
from reel.models import Reels


def home(request):
    posts = BlogPost.objects.all().order_by("-created_on")[:3]
    images = Gallery.objects.all().order_by("-created_on")[:5]
    reels = Reels.objects.all().order_by("-created_on")[:4]
    return render(request, "website/index.html", context={"posts": posts, "images": images, "reels":reels})

