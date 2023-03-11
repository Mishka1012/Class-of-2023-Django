from django.contrib import admin

from .models import Article, Comment, Star

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class RatingsInline(admin.StackedInline):
    model = Star
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
        RatingsInline,
    ]

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
