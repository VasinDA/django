from django.urls import path
from .views import PostsPageView
 
urlpatterns = [
    path("", PostsPageView.as_view(), name="posts"),
]
