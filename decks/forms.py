from django import forms
from .models import DeckPost


class DeckPostForm(forms.ModelForm):
    class Meta:
        model = DeckPost
        fields = ["title", "content", "deck_list"]
