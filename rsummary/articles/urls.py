from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('articles/', views.article_list, name="article-list"),
    path('articles/new', views.ArticleCreateView.as_view(), name="article-create"),
    path('articles/<int:article_id>', views.article_detail, name="article-detail"),
    path('articles/<int:article_id>/edit', views.article_update, name="article-update"),
    path('articles/<int:article_id>/delete', views.article_delete, name="article-delete"),
]
