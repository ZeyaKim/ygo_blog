from django.db import models
from django.utils import timezone


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100, default="General")
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __repr__(self):
        return self.title
