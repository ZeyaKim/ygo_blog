from django.views.generic import ListView, DetailView, CreateView
from decks.models import DeckPost
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin


class DeckListView(ListView):
    model = DeckPost
    template_name = "decks/deck_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return DeckPost.objects.filter(is_deleted=False).order_by("-created_at")


class DeckDetailView(DetailView):
    model = DeckPost
    template_name = "decks/deck_detail.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        if post.is_deleted:
            raise Http404
        return post


class DeckPostCreateView(LoginRequiredMixin, CreateView):
    model = DeckPost
    template_name = "decks/deck_create.html"
    fields = ["title", "content", "image", "tags"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MatchRecordListView(ListView): ...


class MatchRecordDetailView(DetailView): ...


class MatchRecordCreateView(CreateView): ...
