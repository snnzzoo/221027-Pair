from django.db import models
from multiselectfield import MultiSelectField
from django.core.validators import MinValueValidator, MaxValueValidator
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill
from django.conf import settings


# Create your models here.
"""
책 리뷰
- 책 제목
- 작가
- 출판사
- 장르 (다중 선택)
- 작성자
- 작성 시간 , 수정 시간
- 리뷰 제목
- 내용, 줄거리
- 평점 (1~5)
- 이미지, 썸네일 (선택사항)
- 좋아요
- 댓글
"""

class Review(models.Model):
    book = models.CharField(max_length=30)
    writer = models.CharField(max_length=30)
    publisher = models.CharField(max_length=20)
    genrelist = (
        ("소설", "소설"),
        ("시, 수필, 에세이", "시, 수필, 에세이"),
        ("재테크", "재테크"),
        ("철학, 예술, 종교", "철학, 예술, 종교"),
        ("자기계발서", "자기계발서"),
        ("어학, 외국어", "어학, 외국어"),
        ("역사, 인문학", "역사, 인문학"),
        ("가정, 육아, 요리", "가정, 육아, 요리"),
        ("정치, 사회과학", "정치, 사회과학"),
        ("기타", "기타"),
    )
    genre = MultiSelectField(
        choices=genrelist,
        min_choices=1,
        max_choices=3,
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    image = ProcessedImageField(
        blank=True,
        upload_to="images/",
        processors=[ResizeToFill(720, 480)],
        format="JPEG",
        options={"quality": 100},
    )
    thumbnail = ImageSpecField(source='image', 
                                processors=[ResizeToFill(120,80)], 
                                format='JPEG')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)