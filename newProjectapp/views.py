from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import Person


# Create your views here.
def my_func(request):
    obj = place.objects.all()
    Pobj = Person.objects.all()
    return render(request, "index.html", {'place': obj, 'person': Pobj})


def about(request):
    return render(request, "about.html")
