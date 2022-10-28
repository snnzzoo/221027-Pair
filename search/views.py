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
        user = User.objects.all().filter(Q(username__contains=query))
        article = Article.objects.all().filter(
            Q(title__contains=query) | Q(content__contains=query)
        )
        review = Review.objects.all().filter(
            Q(book__contains=query) | Q(writer__contains=query)
        )
    context = {
        "query": query,
        "user": user,
        "article": article,
        "review": review,
    }
    return render(
        request,
        "search/search.html",
        context,
    )
