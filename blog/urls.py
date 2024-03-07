from django.urls import path
from blog.views import BlogListView, BlogDetailView, PostCreateView

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),
    path("<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("write/", PostCreateView.as_view(), name="blog_create"),
]

# Step 1
