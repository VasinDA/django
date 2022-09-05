from django.views.generic import ListView, DetailView
from .models import Message
 
class MessagePageView(ListView):
    model = Message
    template_name = "message.html"

class MessageDetailView(DetailView):
    model = Message
    template_name = "message_detail.html"