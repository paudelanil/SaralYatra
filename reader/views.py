from django.shortcuts import render
from django.views.generic import ListView
from .models import Read


# Create your views here.
class HomePageView(ListView):
    model = Read
    template_name = "home.html"
