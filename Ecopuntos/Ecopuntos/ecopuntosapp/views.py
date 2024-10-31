from django.shortcuts import render


def index(request):
    return render(request, "ecopuntosapp/index.html")


def iniciohtml(request):
    return render(request, "ecopuntosapp/inicio.html")



# Create your views here.
