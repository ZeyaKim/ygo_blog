from django.contrib import admin
from blog.models import BlogPost, BlogComment, BlogSubComment
from decks.models import DeckPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "content", "created_at")


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ("content", "created_at", "author")


class BlogSubCommentAdmin(admin.ModelAdmin):
    list_display = ("content", "created_at", "author")


class DeckPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at", "is_deleted")


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
admin.site.register(BlogSubComment, BlogSubCommentAdmin)
admin.site.register(DeckPost, DeckPostAdmin)
