from blog.models import BlogPost
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from blog.forms import BlogPostForm
from django.http import HttpResponseRedirect


class BlogListView(ListView):
    model = BlogPost
    template_name = "blog/blog_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = BlogPost.objects.all()
        return context


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog/blog_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "blog/blog_write.html"
    # fields = ["title", "category", "content"]
    success_url = "/blog/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "blog/blog_write.html"
    success_url = "/blog/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(DeleteView):
    model = BlogPost

    success_url = "/blog/"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


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
