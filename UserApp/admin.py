from django.contrib import admin
from .models import User, Password

# Register your models here.

admin.site.register(User)
admin.site.register(Password)