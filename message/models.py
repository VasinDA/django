from django.db import models
from django.urls import reverse

class Message(models.Model):
    email = models.EmailField(null=True)
    text = models.TextField()

    def __str__(self) -> str:
        return self.text[:50]

    def get_absolute_url(self):
        return reverse("message_detail", kwargs={"pk":self.pk})