from django.shortcuts import redirect, render
from .models import Objects
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, "ecopuntosapp/ecopuntos.html")

def inicio(request):
    data = {
        "form": CustomUserCreationForm()
    }
    if request.method == "POST":
        formularioreg = CustomUserCreationForm(data= request.POST)
        if formularioreg.is_valid():
            formularioreg.save()
            user = authenticate(username=formularioreg.cleaned_data["username"], email= formularioreg.cleaned_data["email"],
                                 password= formularioreg.cleaned_data["password"])
            login (request,user)
            
            return redirect(to="home")
        data ["form"] = formularioreg


    return render(request, "ecopuntosapp/inicio.html", data)

def faq(request):
    return render(request, "ecopuntosapp/FAQ.html")

def search(request):
    return render(request, "ecopuntosapp/search.html")

def ourselves(request):
    return render(request, "ecopuntosapp/AboutUs.html")

def forums(request):
    return render(request, "ecopuntosapp/forums.html")



# Create your views here.
