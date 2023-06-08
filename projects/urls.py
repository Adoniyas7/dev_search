from django.urls import path
from . import views

urlpatterns = [
    path("nklnln/",views.home, name="home"),
    path("",views.projects, name="projects"),
    path("projects/<str:pk>",views.project, name= "project"),
    path("add_project", views.add_project, name="add_project"),
    path("edit_project/<str:pk>", views.edit_project, name="edit_project"),
]