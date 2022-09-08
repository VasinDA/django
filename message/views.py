from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Message
 
class MessagePageView(ListView):
    model = Message
    template_name = "message.html"

class MessageDetailView(DetailView):
    model = Message
    template_name = "message_detail.html"

class MessageCreateView(CreateView):
    model = Message
    template_name = "message_new.html"
    fields = ["email", "text"]

class MessageUpdateview(UpdateView):
    model = Message
    template_name = "message_edit.html"
    fields = ["text"]

class MessageDeleteView(DeleteView):
    model = Message
    template_name = "message_delete.html"
    success_url = reverse_lazy("message")