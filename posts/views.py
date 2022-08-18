from django.views.generic import ListView
from .models import Post
 
class PostsPageView(ListView):
    model = Post
    template_name = "posts.html"