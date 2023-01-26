from django.shortcuts import render
from django.views.generic import ListView
from . import models


class AniquizListView(ListView):
    model = models.Quiz
    template_name = "home.html"
