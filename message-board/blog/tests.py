from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post

# Create your tests here.
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )

        cls.post = Post.objects.create(
            title="Blog Title",
            body="This is a body content for this blog post.",
            author=cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "Blog Title")
        self.assertEqual(self.post.body, "This is a body content for this blog post.")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "Blog Title")
        self.assertEqual(self.post.get_absolute_url(), "/post/1")

    def test_url_exists_at_correct_location_blog(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detail(self):
        response = self.client.get("/post/1")
        self.assertEqual(response.status_code, 200)

    def test_blog_listview(self):
        responce = self.client.get(reverse("blog_list"))
        self.assertEqual(responce.status_code, 200)
        self.assertContains(responce, "This is a body content for this blog post.")
        self.assertTemplateUsed(responce, "blog_list.html")

    def test_blog_detailview(self):
        responce = self.client.get(reverse("post_detail", kwargs={'pk': self.post.pk}))
        self.assertEqual(responce.status_code, 200)
        self.assertContains(responce, "Blog Title")
        self.assertTemplateUsed(responce, "post-detail.html")
        no_response = self.client.get("/post/0")
        self.assertEqual(no_response.status_code, 404)
