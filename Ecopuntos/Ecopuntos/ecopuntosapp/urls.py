from django.urls import path, include
from .views import inicio

urlpatterns = [
    path ("", inicio, name="inicio")
    ]