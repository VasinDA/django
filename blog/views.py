from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentForm
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy, reverse
from .models import Post

class CommentGet(DetailView):
    model = Post
    template_name = "post_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context
 
class CommentPost(LoginRequiredMixin, SingleObjectMixin, FormView):
    model = Post
    form_class = CommentForm
    template_name = "post_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
            
    def form_valid(self, form):
        form.author = self.request.user
        comment = form.save(commit=False)
        comment.post = self.object
        comment.save()
        return super().form_valid(form)
   
    def get_success_url(self):
        post = self.get_object()
        return reverse("post_detail", kwargs={"pk": post.pk}) 

class BlogListView(ListView):
    model = Post
    template_name = "blog.html"

class BlogDetailView(View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
   
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("blog")