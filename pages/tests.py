from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.
class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    def test_url_avaliable_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "pages/home.html")
    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Welcome to the Home Page</h1>")



class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
    def test_url_avaliable_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "pages/about.html")
    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About Page</h1>")
