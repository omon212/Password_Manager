from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20,unique=True,null=False)
    password = models.CharField(max_length=50,default="Password",null=False)
    email = models.EmailField(max_length=50,unique=True,null=False)

    def __str__(self):
        return self.name


class Password(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="passwords")
    name_of_applications = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    time = models.DateTimeField(auto_now_add=True,null=False)

    def __str__(self):
        return self.name_of_applications

