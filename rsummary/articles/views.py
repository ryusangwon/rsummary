from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.
def article_list(request):
    articles = Article.objects.all()
    context = {}
    context['articles'] = articles
    return render(request, 'articles/article_list.html', context=context)

def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {}
    context['article'] = article
    return render(request, 'articles/article_detail.html', context=context)