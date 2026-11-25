from django.urls import path
from . import views

app_name = "jogos"

urlpatterns = [
    path("", views.lista_jogos, name="lista_jogos"),
]
