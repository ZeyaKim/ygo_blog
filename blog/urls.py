from django.urls import path
from blog.views import BlogListView, BlogDetailView

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),
    path("<int:id>/", BlogDetailView.as_view(), name="blog_detail"),
]
