from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index, save_location, register

urlpatterns = [
    path("", index, name="index"),
    path("save-location/", save_location, name="update_location"),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("accounts/register/", register, name="register"),
]