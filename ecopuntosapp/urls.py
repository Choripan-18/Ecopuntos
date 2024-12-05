from django.urls import path, include
from .views import iniciolog,inicioreg,home,faq,search,forums,ourselves,perfil,impacto
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path ("", home, name="home"),
    path ("login/", iniciolog, name="login"),
    path ("FAQ/", faq, name="faq"),
    path ("search/", search, name="search"),
    path ("forums/", forums, name="forums"),
    path ("ourselves/", ourselves, name="ourselves"),
    path ("profile/", perfil, name="perfil"),
    path ("logout/", LogoutView.as_view(next_page="home"), name="logout"),
    path ("impacto/", impacto, name="impacto")
    ]