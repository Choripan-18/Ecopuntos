from django.urls import path, include
from .views import iniciolog,inicioreg,home,faq,search,forums,ourselves

urlpatterns = [
    path ("", home, name="home"),
    path ("login/", iniciolog, name="login"),
    path ("FAQ/", faq, name="faq"),
    path ("search/", search, name="search"),
    path ("forums/", forums, name="forums"),
    path ("ourselves/", ourselves, name="ourselves")
    ]