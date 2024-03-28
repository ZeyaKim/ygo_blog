from django.views.generic import ListView, DetailView, CreateView
from decks.models import DeckPost, Deck, DeckInDeckPost
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from decks.forms import DeckPostForm
from django.urls import reverse_lazy
import json


class DeckListView(ListView):
    model = DeckPost
    template_name = "decks/deck_list.html"
    context_object_name = "decks"

    def get_queryset(self):
        return DeckPost.objects.filter(is_deleted=False).order_by("-created_at")


class DeckDetailView(DetailView):
    model = DeckPost
    template_name = "decks/deck_detail.html"
    context_object_name = "deck_post"

    def get_object(self, queryset=None):
        # URL로부터 받은 PK를 이용하여 DeckPost 객체를 가져옵니다.
        deck_post = super().get_object(queryset)
        # 삭제된 포스트라면 404 에러를 발생시킵니다.
        if deck_post.is_deleted:
            raise Http404
        return deck_post

    def get_context_data(self, **kwargs):
        # 기본 컨텍스트 데이터를 가져옵니다.
        context = super().get_context_data(**kwargs)
        # 현재 포스트와 연결된 모든 덱을 찾아옵니다.
        deck_in_post = DeckInDeckPost.objects.filter(deck_post=self.get_object())
        # 연관된 덱들의 리스트를 구성합니다.
        decks = [dip.deck_name for dip in deck_in_post]
        # 컨텍스트에 덱 리스트를 추가합니다.
        context["decks"] = decks
        return context


class DeckPostCreateView(LoginRequiredMixin, CreateView):
    model = DeckPost
    form_class = DeckPostForm
    template_name = "decks/deck_write.html"
    success_url = reverse_lazy(
        "deck_list"
    )  # 'deck_list'는 덱 리스트를 보여주는 페이지의 url name

    def form_valid(self, form):
        form.instance.author = (
            self.request.user
        )  # 현재 로그인한 사용자를 덱 포스트의 작성자로 설정
        self.object = form.save()  # 덱 포스트 저장

        # form.cleaned_data에서 덱 데이터를 가져옵니다.
        decks_str = form.cleaned_data[
            "tags"
        ]  # 'decks' 필드는 form에서 문자열로 덱 이름들을 받는다고 가정
        print(decks_str)
        decks_list = json.loads(decks_str)  # JSON 문자열을 파이썬 리스트로 변환
        print(decks_list)
        # 덱 리스트에서 각 덱에 대해 처리
        for deck_map in decks_list:
            deck_name = deck_map["value"]
            deck_name = deck_name.strip()  # 공백 제거
            if deck_name:  # 덱 이름이 비어있지 않은 경우에만 처리
                deck, created = Deck.objects.get_or_create(
                    deck_name=deck_name
                )  # 덱 가져오기, 없으면 생성
                DeckInDeckPost.objects.create(
                    deck_post=self.object, deck_name=deck
                )  # DeckInDeckPost에 연결

        return super().form_valid(form)


class MatchRecordListView(ListView): ...


class MatchRecordDetailView(DetailView): ...


class MatchRecordCreateView(CreateView): ...
