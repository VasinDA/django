from django.urls import path
from .views import MessagePageView, MessageDetailView, MessageCreateView, MessageUpdateview, MessageDeleteView
 
urlpatterns = [
    path("", MessagePageView.as_view(), name="message"),
    path("message/<int:pk>/", MessageDetailView.as_view(), name="message_detail"),
    path("mesasge/new/", MessageCreateView.as_view(), name="message_new"),
    path("mesasge/<int:pk>/edit/", MessageUpdateview.as_view(), name="message_edit"),
    path("mesasge/<int:pk>/delete/", MessageDeleteView.as_view(), name="message_delete"),
]
