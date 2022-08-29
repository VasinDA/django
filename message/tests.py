from django.test import TestCase
from django.urls import reverse
from .models import Message
 
class MessageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.message = Message.objects.create(email="vasinda@service.dp.ua")
        cls.message = Message.objects.create(text="This is a test!")
   
    def test_model_content(self):
        self.assertEqual(self.message.email, "vasinda@service.dp.ua")
        self.assertEqual(self.message.text, "This is a test!")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/message")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse("message"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "message.html")
        self.assertContains(response, "vasinda@service.dp.ua")
        self.assertContains(response, "This is a test!")