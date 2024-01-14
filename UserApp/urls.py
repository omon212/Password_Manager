from django.urls import path
from .views import PasswordGeneratelevel1
urlpatterns = [
    path("password1",PasswordGeneratelevel1.as_view())
]