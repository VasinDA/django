from django.db import models

class Message(models.Model):
    email = models.EmailField(null=True)
    text = models.TextField()

    def __str__(self) -> str:
        return self.text[:50]