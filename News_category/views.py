from django.shortcuts import render
from . import models


# Create your views here.
def daily_news(request):
    all_categories = models.News_category.objects.all()
    news_categories = models.New.objects.all()

    search_new = request.GET.get('pr')
    if search_new:
        all_new_search = models.New.objects.filter(name__contains=search_new)

    context = {'all_categories': all_categories, 'news_categories': news_categories }
    return render(request, 'index.html', context)


def category(request, pk):
    news_categories = models.New.objects.filter(news_category__id=pk)
    context = {'news': news_categories}
    return render(request, 'category.html', context)





