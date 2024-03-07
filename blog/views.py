from django.shortcuts import render


# Create your views here.
def blog_list(request):
    return render(request, "blog_list.html")


def blog_detail(request, id):
    context = {"id": id}
    return render(request, "blog_detail.html", context)
