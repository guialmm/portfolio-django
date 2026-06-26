from django.urls import path
from . import views

urlpatterns = [
    path("", views.hub, name="home"),
    path("projetos/", views.project_list, name="project_list"),
    path("projetos/<slug:slug>/", views.project_detail, name="project_detail"),
    path("stack/", views.stack, name="stack"),
    path("contato/", views.contact, name="contact"),
]
