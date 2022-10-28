from django.shortcuts import render, redirect
from .forms import CommentForm, ReviewForm
from .models import Review, Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    reviews = Review.objects.order_by('-pk')
    paginator = Paginator(reviews, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'reviews': reviews,
        'posts': posts,
    }
    return render(request, 'reviews/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.review = review
            review_form.save()
            messages.success(request, '리뷰 작성 완료!')
            return redirect('reviews:index')
    else:
        review_form = ReviewForm()
    context = {
        'review_form': review_form
    }
    return render(request, 'reviews/create.html', context)


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        'review': review,
        'comments': review.comment_set.all(),
        'comment_form': comment_form,
    }
    return render(request, 'reviews/detail.html', context)


@login_required
def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES, instance=review)
        if review_form.is_valid():
            review_form.save()
            messages.success(request, '리뷰 수정 완료!')
            return redirect('reviews:detail', pk)
    else:
        review_form = ReviewForm(instance=review)
    context = {
        'review_form': review_form
    }
    return render(request, 'reviews/create.html', context)


@login_required
def delete(request, pk):
    Review.objects.get(pk=pk).delete()
    messages.warning(request, '리뷰 삭제 완료!')
    return redirect('reviews:index')


@login_required
def comment_create(request, pk):
    review = Review.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
    return redirect('reviews:detail', pk)


@login_required
def comment_delete(request, review_pk, comment_pk):
    Comment.objects.get(pk=comment_pk).delete()
    return redirect('reviews:detail', review_pk)


@login_required
def like(request, pk):
    review = Review.objects.get(pk=pk)
    # 이미 좋아요를 누른 경우 => 좋아요 취소
    # if request.user in review.like_users.all():
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    return redirect('reviews:detail', pk)
