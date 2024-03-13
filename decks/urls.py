from django.urls import path
from decks.views import (
    DeckListView,
    DeckDetailView,
    DeckPostCreateView,
    MatchRecordListView,
    MatchRecordDetailView,
    MatchRecordCreateView,
)


urlpatterns = [
    path("", DeckListView.as_view(), name="deck_list"),
    path("<int:pk>/", DeckDetailView.as_view(), name="deck_detail"),
    path("deck_post/write/", DeckPostCreateView.as_view(), name="deck_post_write"),
    path("match_record/", MatchRecordListView.as_view(), name="match_record_list"),
    path(
        "match_record/<int:pk>/",
        MatchRecordDetailView.as_view(),
        name="match_record_detail",
    ),
    path(
        "match_record/write/",
        MatchRecordCreateView.as_view(),
        name="match_record_write",
    ),
]

