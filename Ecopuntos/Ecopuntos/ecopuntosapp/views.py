from django.shortcuts import render


def index(request):
    return render(request, "ecopuntosapp/index.html")



# Create your views here.
