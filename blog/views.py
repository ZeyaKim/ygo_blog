from django.shortcuts import render
from blog.models import BlogPost


# Create your views here.
def blog_list(request):
    posts = BlogPost.objects.all()
    context = {"posts": posts}
    return render(request, "blog_list.html", context)


def blog_detail(request, id):
    context = {"id": id}
    return render(request, "blog_detail.html", context)
