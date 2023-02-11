from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePageView(request):
    # do something with request
    return HttpResponse("Hello Django")
