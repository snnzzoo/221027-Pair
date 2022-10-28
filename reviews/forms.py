from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "title",
            "content",
            "rating",
            "image",
            "book",
            "writer",
            "publisher",
            # "genrelist",
            "genre",
        ]
        labels = {
            'title': '리뷰 제목',
            'content': '리뷰 내용',
            'rating': '평점',
            'image': '사진 첨부',
            'book': '책 제목',
            'writer': '작가',
            'publisher': '출판사',
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
