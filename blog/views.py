from blog.models import BlogPost
from django.views.generic import ListView, DetailView


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
        context["id"] = self.kwargs.get("id")
        return context
