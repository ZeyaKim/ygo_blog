from blog.models import BlogPost, BlogComment, BlogSubComment
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
from django.db import transaction


class BlogListView(ListView):
    model = BlogPost
    template_name = "blog/blog_list.html"
    context_object_name = "posts"  # 추가된 컨텍스트 변수명 설정

    def get_queryset(self):
        """
        삭제되지 않은 게시글만 필터링하고, 'order' 매개변수에 따라 결과를 정렬합니다.
        """
        return BlogPost.objects.filter(is_deleted=False).order_by("-created_at")


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


class UpdateCommentView(LoginRequiredMixin, UserPassesTestMixin, View):
    def post(self, request, *args, **kwargs):
        comment_pk = kwargs.get("comment_pk")
        comment = BlogComment.objects.get(pk=comment_pk)

        if not self.has_permission(request, comment):
            return render(request, "blog/blog_deleted_post.html")

        form = BlogCommentForm(request.POST, instance=comment)
        if form.is_valid():
            with transaction.atomic():
                form.save()
                return HttpResponseRedirect("/blog/")
        else:
            return render(request, "blog/comment_update.html", {"form": form})

    def test_func(self):
        comment = BlogComment.objects.get(pk=self.kwargs.get("comment_pk"))
        return self.has_permission(self.request, comment)

    def get_object(self):
        comment_pk = self.kwargs.get("comment_pk")
        post_pk = self.kwargs.get("post_pk")
        try:
            post = BlogPost.objects.get(pk=post_pk)
            return BlogComment.objects.get(pk=comment_pk, post=post)
        except (BlogPost.DoesNotExist, BlogComment.DoesNotExist):
            return None

    def has_permission(self, request, comment):
        return request.user == comment.author


class DeleteCommentView(LoginRequiredMixin, UserPassesTestMixin, View):
    def post(self, request, *args, **kwargs):
        comment_pk = kwargs.get("comment_pk")

        comment = BlogComment.objects.get(pk=comment_pk)
        if not request.user == comment.author:
            return render(request, "blog/blog_deleted_post.html")

        # Delete the comment
        comment.delete()
        return HttpResponseRedirect("/blog/")

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_object(self):
        comment_pk = self.kwargs.get("comment_pk")
        try:
            return BlogComment.objects.get(pk=comment_pk)
        except BlogComment.DoesNotExist:
            return None


class CreateSubCommentView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        comment_pk = kwargs.get("comment_pk")
        try:
            comment = BlogComment.objects.get(pk=comment_pk)
        except BlogComment.DoesNotExist:
            return render(request, "blog/blog_deleted_post.html")

        author = request.user
        content = request.POST.get("reply_content")
        if content:
            subcomment = BlogSubComment(author=author, content=content, comment=comment)
            subcomment.save()
        return HttpResponseRedirect(f"/blog/{comment.post.pk}/")


class UpdateSubCommentView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        subcomment_pk = kwargs.get("subcomment_pk")
        subcomment = BlogSubComment.objects.get(pk=subcomment_pk)
        if not request.user == subcomment.author:
            return render(request, "blog/blog_deleted_post.html")

        form = BlogCommentForm(request.POST, instance=subcomment)
        if form.is_valid():
            with transaction.atomic():
                form.save()
                return HttpResponseRedirect(f"/blog/{subcomment.comment.post.pk}/")
        else:
            return HttpResponseRedirect(f"/blog/{subcomment.comment.post.pk}/")


class DeleteSubCommentView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        subcomment_pk = kwargs.get("subcomment_pk")
        subcomment = BlogSubComment.objects.get(pk=subcomment_pk)
        print(request.user, subcomment.author)
        if not request.user == subcomment.author:
            return render(request, "blog/blog_deleted_post.html")

        # Delete the subcomment
        subcomment.delete()
        return HttpResponseRedirect(f"/blog/{subcomment.comment.post.pk}/")
