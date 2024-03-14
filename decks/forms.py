from django import forms
from .models import DeckPost


class DeckPostForm(forms.ModelForm):
    tags = forms.CharField(required=False)  # 'tags' 필드 추가

    class Meta:
        model = DeckPost
        fields = ["title", "content", "deck_list", "tags"]  # 'tags'를 포함시킴
        widgets = {
            "tags": forms.TextInput(attrs={"data-role": "tagsinput"}),  # 태그 입력용
        }
