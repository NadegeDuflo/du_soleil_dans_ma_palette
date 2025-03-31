from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone

from PIL import Image
from _utils import resize_img, has_changed
import os

from website import settings



User = get_user_model()

class Category(models.Model):

    name = models.CharField(max_length=36, verbose_name="Nom")
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
           self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Catégorie"


class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ManyToManyField(Category, verbose_name="Catégorie", blank=True)
    last_updated = models.DateTimeField(auto_now=True, verbose_name="Dernière mise à jour")
    created_on = models.DateTimeField(default=timezone.now, null=True, verbose_name="Date de publication")
    published = models.BooleanField(default=False, verbose_name="Publié")
    thumbnail = models.ImageField(upload_to='blog')
    alt = models.CharField(default=False, max_length=255, verbose_name="Texte alternatif")
    chapo = models.TextField(verbose_name="Chapô", null=True, blank=True)
    content = RichTextUploadingField(verbose_name="Contenu", null=True)


    class Meta:
        ordering = ['-created_on']
        verbose_name = "Article"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        
        if has_changed(self, "thumbnail"):
            
            filename = os.path.splitext(self.thumbnail.name)[0]
            filename = f"{filename}.jpg"
            
            img = Image.open(self.thumbnail.file)
            
            if img.mode not in ('L', 'RGB'):
                img = img.convert('RGB')
            
            self.thumbnail.save(filename, resize_img(img, (1000,1000)), save=False)
        
        for token in self.content.split():
            # find all <img src="/media/.../img.jpg">
            if token.startswith('src='):
                filepath = token.split('=')[1].strip('"')   # get path of src
                filepath = filepath.replace('/media', str(settings.MEDIA_ROOT))  # resolve path to MEDIA_ROOT
                print(filepath)
                img = Image.open(str(filepath))
                img.thumbnail((1000,1000))
                img.save(filepath)
        
        if not self.slug:
           self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    @property
    def author_or_default(self):
        return self.author.username if self.author else "Auteur inconnu"

    def get_absolute_url(self):
        return reverse('blog:home')

    def get_category(self):
        return ", ".join(category.name for category in self.category.all())

    get_category.short_description = 'Catégorie'

    def get_comments(self):
        return self.comments.exclude(status=Comment.STATUS_HIDDEN).order_by('-created_on')


class Comment(models.Model):
    STATUS_VISIBLE = 'visible'
    STATUS_HIDDEN = 'hidden'
    STATUS_MODERATED = 'moderated'

    STATUS_CHOICES = (
        (STATUS_VISIBLE, 'visible'),
        (STATUS_HIDDEN, 'hidden'),
        (STATUS_MODERATED, 'moderated'),
    )

    post = models.ForeignKey('BlogPost', on_delete=models.CASCADE, verbose_name="Articles", related_name="comments")
    author_comment = models.CharField(max_length=100, verbose_name="Auteur")
    content_comment = models.TextField(verbose_name="Contenu")
    status = models.CharField(max_length=20, default=STATUS_VISIBLE, choices=STATUS_CHOICES, verbose_name="Statut")
    moderation_text = models.CharField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Date de publication")

    class Meta:
        verbose_name = 'Commentaire'

    def __str__(self):
        return f'{self.author_comment} - {self.content_comment[:8]} statut : {self.status}'

    def get_answers(self):
        return self.answers.exclude(status=Reply.STATUS_HIDDEN)



class Reply(models.Model):
    STATUS_VISIBLE = 'visible'
    STATUS_HIDDEN = 'hidden'
    STATUS_MODERATED = 'moderated'

    STATUS_CHOICES = (
        (STATUS_VISIBLE, 'visible'),
        (STATUS_HIDDEN, 'hidden'),
        (STATUS_MODERATED, 'moderated'),
    )

    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, verbose_name="Commentaire", related_name="answers")
    author_answer = models.CharField(max_length=100, verbose_name="Auteur")
    content_answer = models.TextField(verbose_name="Contenu")
    status = models.CharField(max_length=20, default=STATUS_VISIBLE, choices=STATUS_CHOICES, verbose_name="Statut")
    moderation_text_answer = models.CharField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Date de publication")

    class Meta:
        verbose_name = 'Réponse'

    def __str__(self):
        return f'{self.author_answer} - {self.content_answer[:8]}'


