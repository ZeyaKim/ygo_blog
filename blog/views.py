from blog.models import BlogPost
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from blog.forms import BlogPostForm
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.http import Http404


class BlogListView(ListView):
    model = BlogPost
    template_name = "blog/blog_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = BlogPost.objects.filter(is_deleted=False)
        return context


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog/blog_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
    # fields = ["title", "category", "content"]
    success_url = "/blog/"
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    # TODO add picture upload

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
