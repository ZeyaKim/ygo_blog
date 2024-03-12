from django import forms
from blog.models import BlogPost, BlogComment


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ["title", "category", "content", "image"]


class BlogCommentForm(forms.ModelForm):

    class Meta:
        model = BlogComment
        fields = ["content"]
