import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class ArticleFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date", lookup_expr="gte")
    end_date = DateFilter(field_name="date", lookup_expr="lte")
    search = CharFilter(field_name="body", lookup_expr="icontains")
    class Meta:
        model = Article
        fields = ["author", ]