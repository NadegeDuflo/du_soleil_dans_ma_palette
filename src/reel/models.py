import os
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone

from _utils import has_changed, resize_img
from PIL import Image




class Reels(models.Model):
    title = models.CharField(max_length=40, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    created_on = models.DateTimeField(default=timezone.now, null=True, verbose_name="Date de publication")
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.CharField(max_length=255, blank=True, verbose_name="Contenu")
    image_reel = models.ImageField(upload_to='reel')
    alt = models.CharField(default=False, max_length=255, verbose_name="Texte alternatif")

    class Meta:
        ordering = ['-created_on']
        verbose_name = "Reel"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if has_changed(self, "image_reel"):
            
            filename = os.path.splitext(self.image_reel.name)[0]
            filename = f"{filename}.jpg"
            
            img = Image.open(self.image_reel.file)
            
            if img.mode not in ('L', 'RGB'):
                img = img.convert('RGB')
            
            self.image_reel.save(filename, resize_img(img, (500,500)), save=False)
            
        
        
        if not self.slug:
           self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('home')
