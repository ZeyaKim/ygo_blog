from django.urls import path
from blog.views import (
    BlogListView,
    BlogDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    BlogSearchView,
)

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),
    path("<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("write/", PostCreateView.as_view(), name="blog_write"),
    path("edit/<int:pk>/", PostUpdateView.as_view(), name="blog_edit"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="blog_delete"),
    path("search/<str:category>", BlogSearchView.as_view(), name="blog_search"),
    # path()
]

# Step 1
