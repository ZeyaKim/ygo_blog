from blog.models import BlogPost, BlogComment
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from blog.forms import BlogPostForm, BlogCommentForm
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.http import Http404
from django.views import View


class BlogListView(ListView):
    model = BlogPost
    template_name = "blog/blog_list.html"
    context_object_name = "posts"  # 추가된 컨텍스트 변수명 설정

    def get_queryset(self):
        """
        삭제되지 않은 게시글만 필터링하고, 'order' 매개변수에 따라 결과를 정렬합니다.
        """
        order = self.request.GET.get(
            "order", "created_at"
        )  # 기본값으로 'created_at' 사용
        if order not in ["created_at", "-created_at", "views", "-views"]:
            order = "created_at"  # 유효하지 않은 정렬 키가 주어진 경우 기본값을 사용
        return BlogPost.objects.filter(is_deleted=False).order_by(order)

    def get_context_data(self, **kwargs):
        """
        필요한 추가 컨텍스트 변수들을 여기에 정의합니다.
        """
        context = super().get_context_data(**kwargs)
        context["order"] = self.request.GET.get(
            "order", "created_at"
        )  # 현재 정렬 기준을 컨텍스트에 추가
        return context


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog/blog_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = BlogCommentForm()
        return context

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            return render(request, "blog/blog_deleted_post.html")

        if self.object.is_deleted:
            return render(request, "blog/blog_deleted_post.html")
        context = self.get_context_data(object=self.object)
        self.object.views += 1
        self.object.save()
        return self.render_to_response(context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "blog/blog_write.html"
    success_url = "/blog/"
    login_url = "/login/"
    redirect_field_name = "redirect_to"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "blog/blog_write.html"
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    success_url = "/blog/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    login_url = "/login/"
    success_url = "/blog/"
    fields = ["is_deleted"]

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_deleted = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class BlogSearchView(ListView):
    model = BlogPost
    template_name = "blog/blog_search_list.html"
    context_object_name = "results"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filetr_func_list = [
            self.search_by_category,
            self.order_by_created_at,
        ]

    def get_queryset(self):
        queryset = BlogPost.objects.all()
        for func in self.filetr_func_list:
            queryset = func(queryset)
        return queryset

    def search_by_category(self, queryset):
        category = self.kwargs.get("category")
        if category:
            queryset = queryset.filter(category=category)
        return queryset

    def order_by_created_at(self, queryset):
        key = self.request.GET.get("order", "-")
        return queryset.order_by(f"{key}created_at")

    def order_by_views(self, queryset):
        key = self.request.GET.get("order", "-")
        return queryset.order_by(f"{key}views")


class PostRestoreView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    fields = ["is_deleted"]
    login_url = "/login/"
    success_url = "/blog/"

    def post(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            return render(request, "blog/blog_deleted_post.html")

        self.object.is_deleted = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def test_func(self):
        return self.request.user == self.get_object().author


class CreateCommentView(LoginRequiredMixin, View):
    success_url = "/blog/"

    def post(self, request, *args, **kwargs):
        posts_pk = kwargs.get("pk")
        try:
            post = BlogPost.objects.get(pk=posts_pk)
        except Http404:
            return render(request, "blog/blog_deleted_post.html")
        if post.is_deleted:
            return render(request, "blog/blog_deleted_post.html")

        self.success_url = f"/blog/{posts_pk}/"

        author = request.user
        content = request.POST.get("content")
        if content:
            comment = BlogComment(author=author, content=content, post=post)
            comment.save()
            return HttpResponseRedirect(self.success_url)
        else:
            return HttpResponseRedirect(self.success_url)
