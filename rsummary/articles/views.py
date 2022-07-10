from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm

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

def article_create(request):
    if request.method == "POST":
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            new_article = article_form.save()
            return redirect('article-detail', article_id=new_article.id)
    else:
        article_form = ArticleForm()
    context = {}
    context['form'] = article_form
    return render(request, "articles/article_form.html", context=context)

def article_update(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == "POST":
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('article-detail', article_id=article.id)
    else:
        article_form = ArticleForm(instance=article)
    context = {}
    context["form"] = article_form
    return render(request, "articles/article_form.html", context=context)