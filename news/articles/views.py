from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
import requests

from .models import Article
from .forms import CommentForm, RatingForm
from .filters import ArticleFilter


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "article_new.html"
    fields = (
        "image",
        "title",
        "body",
        "address",
    )
    def form_valid(self, form):
        form.instance.author = self.request.user
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": form.instance.address,
            "format": "json",
            "polygon": 0,
            "addressdetails": 0
        }
        request = requests.get(url, params)
        json = request.json()[0]
        form.instance.lat = float(json["lat"])
        form.instance.lon = float(json["lon"])
        return super().form_valid(form)

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects
        my_filter = ArticleFilter(self.request.GET, queryset=articles)
        context['filter'] = my_filter
        if self.request.GET:
            articles = my_filter.qs
            context["article_list"] = articles
        if articles.first():
            first_article_date = articles.first().date
            last_article_date = articles.last().date
            context["start_date"] = 10000 * first_article_date.year + 100 * first_article_date.month + first_article_date.day
            context["end_date"] = 10000 * last_article_date.year + 100 * last_article_date.month + last_article_date.day
        return context

class CommentGet(DetailView):
    model = Article
    template_name = "article_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['rating_form'] = RatingForm()
        return context

class CommentPost(SingleObjectMixin, FormView):
    model = Article
    form_class = CommentForm
    template_name = "article_detail.html"
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)
    def get_success_url(self):
        article = self.get_object()
        return reverse("article_detail", kwargs={"pk": article.pk})

class RatingPost(SingleObjectMixin, FormView):
    model = Article
    form_class = RatingForm
    template_name = "article_detail.html"
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def form_valid(self, form):
        rating = form.save(commit=False)
        rating.article = self.object
        rating.save()
        return super().form_valid(form)
    def get_success_url(self):
        article = self.get_object()
        return reverse("article_detail", kwargs={"pk": article.pk})

class ArticleDetailView(View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'rating' in request.POST:
            view = RatingPost.as_view()
        elif 'comment' in request.POST:
            view = CommentPost.as_view()
        return view(request, *args, **kwargs)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = (
        "image",
        "title",
        "body",
        "address",
    )
    template_name = "article_edit.html"
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def form_valid(self, form):
        if self.object.address == form.instance.address:
            return super().form_valid(form)
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": form.instance.address,
            "format": "json",
            "polygon": 0,
            "addressdetails": 0
        }
        request = requests.get(url, params)
        json = request.json()[0]
        form.instance.lat = float(json["lat"])
        form.instance.lon = float(json["lon"])
        return super().form_valid(form)

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user