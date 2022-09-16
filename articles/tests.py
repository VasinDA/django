from re import A
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Article
 
class ArticleTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )
       
        cls.article = Article.objects.create(
            title="A good title",
            body="Nice body content",
            author=cls.user,
        )
   
    def test_article_model(self):
        self.assertEqual(self.article.title, "A good title")
        self.assertEqual(self.article.body, "Nice body content")
        self.assertEqual(self.article.author.username, "testuser")
        self.assertEqual(str(self.article), "A good title")
        self.assertEqual(self.article.get_absolute_url(), "/articles/article/1/")
    
    def test_article_createview(self):
        response = self.client.post(
            reverse("article_new"),
            {
                "title": "New title",
                "body": "New text",
                "author": self.user.id,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Article.objects.last().title, "New title")
        self.assertEqual(Article.objects.last().body, "New text")
   
    def test_article_updateview(self):
        response = self.client.post(
            reverse("article_edit", args="1"),
            {
                "title": "Updated title",
                "body": "Updated text",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Article.objects.last().title, "Updated title")
        self.assertEqual(Article.objects.last().body, "Updated text")
       
    def test_article_deleteview(self):
        response = self.client.post(reverse("article_delete", args="1"))
        self.assertEqual(response.status_code, 302)
