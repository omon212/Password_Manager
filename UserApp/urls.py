from django.urls import path
from .views import *


urlpatterns = [
    path("password1/",PasswordGeneratelevel1.as_view()),
    path("password2/",PasswordGenerateLevel2.as_view()),
    path("password3/", PasswordGeneratelevel3.as_view()),
    path("register/",UserRegisterView.as_view()),
    path("login/",UserLoginView.as_view()),
    path("app/",UserApplicationVIew.as_view()),
    path("showalluser/",Show_All_Userpasswrod.as_view())
]
