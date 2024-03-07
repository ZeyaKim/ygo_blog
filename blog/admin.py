from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "content")


# Register your models here.
admin.site.register(BlogPost)
