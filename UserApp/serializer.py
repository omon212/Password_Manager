from rest_framework.serializers import ModelSerializer
from .models import User
class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserLoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['name','password']