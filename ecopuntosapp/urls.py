from django.urls import path, include
from .views import inicio,home,faq,search,forums,ourselves

urlpatterns = [
    path ("", home, name="home"),
    path ("home/", home, name="home"),
    path ("login/", inicio, name="login"),
    path ("FAQ/", faq, name="faq"),
    path ("search/", search, name="search"),
    path ("forums/", forums, name="forums"),
    path ("ourselves/", ourselves, name="ourselves")
    ]