from django.views.generic import ListView
from .models import Message
 
class MessagePageView(ListView):
    model = Message
    template_name = "message.html"