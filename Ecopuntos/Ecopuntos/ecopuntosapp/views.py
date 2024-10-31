from django.shortcuts import render

def home(request):
    return render(request, "ecopuntosapp/ecopuntos.html")

def inicio(request):
    return render(request, "ecopuntosapp/inicio.html")



# Create your views here.
