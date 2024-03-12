from django.contrib import admin
from .models import BlogPost, BlogComment, BlogSubComment


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "content", "created_at")


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ("content", "created_at", "author")


class BlogSubCommentAdmin(admin.ModelAdmin):
    list_display = ("content", "created_at", "author")


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
admin.site.register(BlogSubComment, BlogSubCommentAdmin)
