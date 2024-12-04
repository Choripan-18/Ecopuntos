from django.shortcuts import redirect, render
from .models import Objects
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def home(request):
    return render(request, "ecopuntosapp/ecopuntos.html")

def iniciolog(request):
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username = form.cleaned_data['username'],
                                password = form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect("home")
                else:
                    return HttpResponse("usuario no activo")
            else:
                return HttpResponse("la informacion no es correcta")
    else:
        form = LoginForm()
        return render(request, "ecopuntosapp/inicio.html", {"form": form})
    


def inicioreg(request):
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
            
            return redirect(to="{% url 'home' %}")
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

def perfil(request):
    return render(request, "ecopuntosapp/perfil.html")



# Create your views here.
