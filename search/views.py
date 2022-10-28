from django.shortcuts import render
from reviews.models import Review
from articles.models import Article
from accounts.models import User
from django.db.models import Q

# Create your views here.


def searchResult(request):
    user = None
    article = None
    review = None
    query = None
    if "q" in request.GET:
        query = request.GET.get("q")
        user = User.objects.all().filter(
            Q(name__contains=query) | Q(description__contains=query)
        )
        article = Article.objects.all().filter(
            Q(name__contains=query) | Q(description__contains=query)
        )
        review = Review.objects.all().filter(
            Q(name__contains=query) | Q(description__contains=query)
        )
    return render(
        request,
        "search/search.html",
        {"query": query, "user": user, "article": article, "review": review},
    )
