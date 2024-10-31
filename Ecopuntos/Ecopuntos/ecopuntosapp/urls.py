from django.urls import path, include
from .views import inicio,home

urlpatterns = [
    path ("", home, name="home"),
    path ("login/", inicio, name="login")
    ]