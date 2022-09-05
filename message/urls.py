from django.urls import path
from .views import MessagePageView, MessageDetailView
 
urlpatterns = [
    path("", MessagePageView.as_view(), name="message"),
    path("message/<int:pk>/", MessageDetailView.as_view(), name="message_detail"),
]
