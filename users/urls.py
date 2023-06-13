from django.urls import path
from . import views

urlpatterns = [
    path("", views.profiles, name="profiles"),
    path("profile/<str:pk>", views.user_profile, name="user-profile"),
    path("login/", views.login_users, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("account", views.user_account, name="user-account"),
    path("edit-account", views.edit_account, name='edit-account'),
    path("add-skill", views.add_skill, name='add-skill'),
    path("edit-skill/<str:pk>", views.edit_skill, name='edit-skill'),
    path("delete-skill/<str:pk>", views.delete_skill, name='delete-skill'),
]