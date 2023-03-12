import django_filters
from django_filters import DateFilter, CharFilter, FilterSet, NumberFilter
from django.contrib.postgres.search import SearchVector, SearchQuery
from .models import *
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point

class ArticleFilter(FilterSet):
    start_date = DateFilter(field_name="date", lookup_expr="gte")
    end_date = DateFilter(field_name="date", lookup_expr="lte")
    search = django_filters.CharFilter(method="search_filter")
    def search_filter(self, queryset, name, value):
        search_vector = SearchVector("title", "body", "date")
        search_query = SearchQuery(value)
        return queryset.annotate(search=search_vector).filter(search=search_query)

    latitude = NumberFilter(field_name="location__latitude")
    longitude = NumberFilter(field_name="location__longitude")
    radius = NumberFilter(method="radius_filter", label="Radius (km)")

    def radius_filter(self, queryset, name, value):
        point = Point(float(self.data["longitude"]), float(self.data["latitude"]), srid=4326)
        return queryset.annotate(distance=Distance("location", point)).filter(distance__lte=value * 1000)


    class Meta:
        model = Article
        fields = ["author", ]