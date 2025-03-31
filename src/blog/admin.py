
from django.contrib import admin

from blog.models import BlogPost, Category, Comment, Reply


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "published",
        "get_category",
        "created_on",
        "comments_count",
    )

    list_editable = ("published", )

    list_filter = (
        "published",
        "category__name"
    )

    def comments_count(self, post):
        return len(Comment.objects.filter(post=post))

    comments_count.short_description = "Commentaires"







class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ["name"]

class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "post",
        "author_comment",
        "content_comment",
        "status",
        "created_on",
        "answers_count",
    )

    list_editable = ("status", )
    list_filter = (
        "post",
        "status",
    )
    def answers_count(self, comment):
        return len(Reply.objects.filter(comment=comment))

    answers_count.short_description = "Réponses"

class ReplyAdmin(admin.ModelAdmin):
    list_display = (
        "comment",
        "author_answer",
        "content_answer",
        "status",
        "created_on",
    )
    list_editable = ("status",)




admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply, ReplyAdmin)
