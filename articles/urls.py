from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreatelView, ArticleUpdateView, ArticleDeleteView
 
urlpatterns = [
    path("", ArticleListView.as_view(), name="article_list"),
    path("article/<int:pk>/", ArticleDetailView.as_view(), name = "article_detail"),
    path("article/new/", ArticleCreatelView.as_view(), name = "article_new"),
    path("article/<int:pk>/edit/", ArticleUpdateView.as_view(), name = "article_edit"),
    path("article/<int:pk>/delete/", ArticleDeleteView.as_view(), name = "article_delete"),
]
