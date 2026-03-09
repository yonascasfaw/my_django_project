from django.shortcuts import render
from django.views.generic.base import TemplateView


def index(request):
    print(request.user)
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")

