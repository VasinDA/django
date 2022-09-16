from django.test import SimpleTestCase
from django.urls import reverse

class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")
    
    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h2>Home page</h2>")


class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h2>About page</h2>")

class ContactspageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/contacts/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("contacts"))
        self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self):
        response = self.client.get(reverse("contacts"))
        self.assertTemplateUsed(response, "contacts.html")

    def test_template_content(self):
        response = self.client.get(reverse("contacts"))
        self.assertContains(response, "<h2>Contacts</h2>")
        self.assertContains(response, '<input type="text" id="Name" name="Name">')
        self.assertContains(response, '<textarea name="Text" id="Text" cols="30" rows="10">')