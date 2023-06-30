from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('projects/', views.projects),
    path('projects/<str:pk>/', views.project),
]