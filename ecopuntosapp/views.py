from django.shortcuts import render

def home(request):
    return render(request, "ecopuntosapp/ecopuntos.html")

def inicio(request):
    return render(request, "ecopuntosapp/inicio.html")

def faq(request):
    return render(request, "ecopuntosapp/FAQ.html")

def search(request):
    return render(request, "ecopuntosapp/search.html")

def ourselves(request):
    return render(request, "ecopuntosapp/AboutUs.html")

def forums(request):
    return render(request, "ecopuntosapp/forums.html")



# Create your views here.
