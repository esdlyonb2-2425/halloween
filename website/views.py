from django.http import HttpResponse
from django.shortcuts import render

from website.models import Truc


# Create your views here.
def test(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    trucs= Truc.objects.all()
    return render(request, "website/autretruc.html", {"trucs":trucs})


def truc(request):
    return HttpResponse("coucou")