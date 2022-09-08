from django.test import TestCase
from django.urls import reverse
from .models import Message
 
class MessageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.message = Message.objects.create(
            email="vasinda@service.dp.ua",
            text="This is a test!"
            )
           
    def test_model_content(self):
        self.assertEqual(self.message.text, "This is a test!")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/message/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse("message"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "message.html")
        self.assertContains(response, "vasinda@service.dp.ua")
        self.assertContains(response, "This is a test!")
        self.assertEqual(self.message.get_absolute_url(), "/message/message/1/")
    
    def test_message_createview(self):
        response = self.client.post(
            reverse("message_new"),
            {
                "email": "den2001@ukr.net",
                "text": "New text",
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Message.objects.last().email, "den2001@ukr.net")
        self.assertEqual(Message.objects.last().text, "New text")
   
    def test_message_updateview(self):
        response = self.client.post(
            reverse("message_edit", args="1"),
            {
                "text": "Updated text",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Message.objects.last().text, "Updated text")
       
    def test_message_deleteview(self):
        response = self.client.post(reverse("message_delete", args="1"))
        self.assertEqual(response.status_code, 302)