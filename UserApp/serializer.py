from rest_framework.serializers import ModelSerializer
from .models import User, Password


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserLoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['name','password']


class UserApplication(ModelSerializer):
    class Meta:
        model = Password
        fields = '__all__'



class PasswordSerializer(ModelSerializer):
    class Meta:
        model = Password
        fields = '__all__'

