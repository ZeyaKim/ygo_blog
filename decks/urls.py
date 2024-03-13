from django.urls import path
from decks.views import DeckListView
from decks.views import DeckDetailView

urlpatterns = [
    path("", DeckListView.as_view(), name="deck_list"),
    path("<int:pk>/", DeckDetailView.as_view(), name="deck_detail"),
]
