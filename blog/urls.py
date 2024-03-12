from django.urls import path
from blog.views import (
    BlogListView,
    BlogDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    BlogSearchView,
    CreateCommentView,
    UpdateCommentView,
    DeleteCommentView,
    CreateSubCommentView,
    UpdateSubCommentView,
    DeleteSubCommentView,
)

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),
    path("<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("write/", PostCreateView.as_view(), name="blog_write"),
    path("edit/<int:pk>/", PostUpdateView.as_view(), name="blog_edit"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="blog_delete"),
    path("search/<str:category>", BlogSearchView.as_view(), name="blog_search"),
    path("restore/<int:pk>/", BlogDetailView.as_view(), name="blog_restore"),
    path("comment/write/<int:pk>/", CreateCommentView.as_view(), name="comment_write"),
    path(
        "comment/edit/<int:comment_pk>/",
        UpdateCommentView.as_view(),
        name="comment_edit",
    ),
    path(
        "comment/delete/<int:comment_pk>/",
        DeleteCommentView.as_view(),
        name="comment_delete",
    ),
    path(
        "subcomment/write/<int:comment_pk>/",
        CreateSubCommentView.as_view(),
        name="subcomment_write",
    ),
    path(
        "subcomment/edit/<int:subcomment_pk>/",
        UpdateSubCommentView.as_view(),
        name="subcomment_edit",
    ),
    path(
        "subcomment/delete/<int:subcomment_pk>/",
        DeleteSubCommentView.as_view(),
        name="subcomment_delete",
    ),
]

# Step 3
