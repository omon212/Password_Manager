from django.shortcuts import render
from .models import User, Password
from rest_framework.views import APIView
from rest_framework.response import Response
import random
from .serializer import UserRegisterSerializer, UserLoginSerializer, UserApplication


class PasswordGeneratelevel1(APIView):
    def get(self, request):
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z",
                    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
                    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                    "U", "V", "W", "X", "Y", "Z"]

        passwordlevel1 = ""
        for i in range(8):
            passwordlevel1 += random.choice(alphabet)
        return Response({"password": passwordlevel1}, status=200)


class PasswordGenerateLevel2(APIView):
    def get(self, request):
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z",
                    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
                    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                    "U", "V", "W", "X", "Y", "Z",
                    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";"]
        passwordlevel2 = ""
        for i in range(4):
            passwordlevel2 += random.choice(alphabet[26:35])
        for d in range(2):
            passwordlevel2 += random.choice(alphabet[62:])
        for c in range(2):
            passwordlevel2 += random.choice(alphabet)
        return Response({"password": passwordlevel2}, status=200)


class PasswordGeneratelevel3(APIView):
    def get(self, request):
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z",
                    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
                    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                    "U", "V", "W", "X", "Y", "Z",
                    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";"]

        passwordlevel3 = ""
        for i in range(2):
            passwordlevel3 += random.choice(alphabet[26:35])
        for d in range(2):
            passwordlevel3 += random.choice(alphabet[62:])
        for c in range(6):
            passwordlevel3 += random.choice(alphabet)

        return Response({"password": passwordlevel3}, status=200)


class UserRegisterView(APIView):
    serializer_class = UserRegisterSerializer  # Use serializer_class instead of serializer
    queryset = User.objects.all()  # Add this line to retrieve all users

    def post(self, request):
        serializer_class = UserRegisterSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({"message": "User Created"})
        else:
            return Response(serializer_class.errors)


class UserLoginView(APIView):
    serializer = UserLoginSerializer
    queryset = User.objects.all()

    def post(self, request):
        username = request.data.get("name")
        password = request.data.get("password")
        serializer = UserLoginSerializer(data=request.data)
        user = User.objects.filter(name=username, password=password)
        if user:
            return Response({"message": "Login Success"}, status=200)
        else:
            return Response(serializer.errors, status=400)


class UserApplicationVIew(APIView):
    serializer_class = UserApplication
    queryset = Password.objects.all()

    def post(self, request):
        serializer = UserApplication(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User Password created successfully"}, status=200)
        else:
            return Response(serializer.errors, status=400)
