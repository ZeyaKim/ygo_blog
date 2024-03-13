from django.db import models


# Create your models here.
class DeckPost(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    deck_list_img = models.ImageField(upload_to="decks", blank=True, null=True)

    def __repr__(self):
        return self.name


class Deck(models.Model):
    deck_name = models.CharField(max_length=100)
