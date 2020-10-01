from django.shortcuts import render
from shopApp import models

def index(request):
    latest_news =models.New
    return render(request, "index.html")
# Create your views here.
