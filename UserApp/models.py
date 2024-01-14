from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20,unique=True,null=False)
    password = models.CharField(max_length=50,default="Password",null=False)
    email = models.EmailField(max_length=50,unique=True,null=False)

