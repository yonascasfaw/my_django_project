from django.shortcuts import render
from django.views.generic.base import TemplateView


from .forms import TechnologyForm

def technology(request):

    if request.method == "GET":
        form = TechnologyForm()
    elif request.method == "POST":
        form = TechnologyForm(request.POST)
        if form.is_valid():
            pass
    else:
        raise NotImplementedError
        

    return render(request, "technology.html", {"form": form})