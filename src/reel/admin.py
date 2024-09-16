from django.contrib import admin

from reel.models import Reels



class ReelAdmin(admin.ModelAdmin):
    list_display = ("title", "published", )
    list_editable = ("published", )


admin.site.register(Reels, ReelAdmin)
