from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from PIL import Image
from _utils import resize_img, has_changed
import os



User = get_user_model()

class Gallery(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    created_on = models.DateTimeField(default=timezone.now, null=True, verbose_name="Date de publication")
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.CharField(max_length=255, blank=True, verbose_name="Contenu")
    image = models.ImageField(upload_to='gallery')
    alt = models.CharField(default=False, max_length=255, verbose_name="Texte alternatif")

    class Meta:
        ordering = ['-created_on']
        verbose_name = "Image"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if has_changed(self, "image"):
            
            filename = os.path.splitext(self.image.name)[0]
            filename = f"{filename}.jpg"
            
            img = Image.open(self.image.file)
            
            if img.mode not in ('L', 'RGB'):
                img = img.convert('RGB')
            
            self.image.save(filename, resize_img(img, (1000,1000)), save=False)
            
        
        
        if not self.slug:
           self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('home')




   

