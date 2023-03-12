from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db.models import Avg
import requests

# Create your models here.
class Article(models.Model):
    image = models.ImageField(upload_to='images/', default='images/placeholder.jpg', blank=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    address = models.CharField(max_length=500, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})
    def average_rating(self):
        avg_rating = 0
        if len(Star.objects.filter(article=self)):
            avg_rating = Star.objects.filter(article=self).aggregate(avg_rating=Avg('rating'))['avg_rating'] / 5 * 100
        return avg_rating

class Star(models.Model):
    rating = models.IntegerField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    article = models.ForeignKey(Article, on_delete=models.CASCADE,)
    comment = models.CharField(max_length=140)
    def __str__(self):
        return self.comment
    def get_absolute_url(self):
        return reverse("article_list")