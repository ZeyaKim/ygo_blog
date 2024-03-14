from django.db import models
from django.conf import settings
from django.urls import reverse


class Deck(models.Model):
    deck_name = models.CharField(max_length=100, unique=True)  # 덱 이름은 고유해야 함

    def __repr__(self):
        return self.deck_name


class DeckPost(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    deck_list = models.ImageField(upload_to="decks/images/")

    def get_absolute_url(self):
        return reverse("deck_detail", args=[self.id])

    def __repr__(self):
        return self.title


class DeckInDeckPost(models.Model):
    deck_post = models.ForeignKey(DeckPost, on_delete=models.CASCADE)
    deck_name = models.ForeignKey(Deck, on_delete=models.CASCADE)

    def __repr__(self):
        return f"{self.deck_post.title} - {self.deck_name.deck_name}"
