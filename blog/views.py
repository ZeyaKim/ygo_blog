from blog.models import BlogPost
from django.views.generic import ListView, DetailView, CreateView


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
    template_name = "blog/post_create.html"
    fields = ["title", "category", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
