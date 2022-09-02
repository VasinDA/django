from django.db import models
from django.urls import reverse
 
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField()
 
    def __str__(self) -> str:
        return self.title[:50]
 
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk":self.pk})