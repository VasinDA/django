from django.urls import path
from .views import MessagePageView
 
urlpatterns = [
    path("", MessagePageView.as_view(), name="message"),
]
