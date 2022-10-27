from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "book",
            "writer",
            "publisher",
            # "genrelist",
            "genre",
            "title",
            "content",
            "rating",
            "image",
        ]
        labels = {
            'genre': 'Genre',
        }
        widgets = {
            "rating": forms.NumberInput(
                attrs={
                    "maxlength": "1",
                    "max": "5",
                    "min": "1",
                }
            ),
        }


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "댓글을 남겨보세요 💬",
            }
        ),
    )
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
