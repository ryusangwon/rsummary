from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm
from django.core.paginator import Paginator

# Create your views here.
def article_list(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 6)
    curr_page_number = request.GET.get('page')
    if curr_page_number is None:
        curr_page_number = 1
    page = paginator.page(curr_page_number)
    
    context = {}
    context['page'] = page
    return render(request, 'articles/article_list.html', context=context)

def article_detail(request, article_id):
    # try:
    #     article = Article.objects.get(id=article_id)
    # except Article.DoesNotExist:
    #     raise Http404()
    article = get_object_or_404(Article, id=article_id)
    
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
    article = get_object_or_404(Article, id=article_id)
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

def article_delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method=="POST":
        article.delete()
        return redirect('article-list')
    else:
        context={}
        context['article'] = article
        return render(request, 'articles/article_confirm_delete.html', context=context)

def index(request):
    return redirect("article-list")