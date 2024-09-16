
from django.contrib import admin

from gallery.models import Gallery


class GalleryPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "created_on", )
    list_editable = ("published", )


admin.site.register(Gallery, GalleryPostAdmin)