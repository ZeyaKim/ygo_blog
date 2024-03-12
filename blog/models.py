from django.db import models
from django.utils import timezone

from django.conf import settings


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="1"
    )
    category = models.CharField(max_length=100, default="General")
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images/", blank=True, null=True)

    def __repr__(self):
        return self.title


class BlogComment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="0"
    )
    post = models.ForeignKey(
        "blog.BlogPost", on_delete=models.CASCADE, related_name="comments"
    )

    def __repr__(self):
        return self.content


class BlogSubComment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="0"
    )
    comment = models.ForeignKey(
        "blog.BlogComment", on_delete=models.CASCADE, related_name="subcomments"
    )

    def __repr__(self):
        return self.content
