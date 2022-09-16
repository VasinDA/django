from django.db import models
from django.urls import reverse
 
class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title[:50]
 
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk":self.pk})

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
   
    def __str__(self):
        return self.comment
   
    def get_absolute_url(self):
        return reverse("article_list")