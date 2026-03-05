from django.shortcuts import render
from django.views.generic.base import TemplateView




def contact(request):
    return render(request, "contact.html")
