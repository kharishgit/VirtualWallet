from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import LoginSerializer
from rest_framework.views import APIView
from django.contrib.auth import login
from accounts.api.serializers import UserSerializer
from accounts.models import User

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user:
            return Response({"success": "User  created successfully"})

class LoginView(APIView):
    def post(self, request):
        print("Hii")

        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            print("Hii")
            user = serializer.validated_data['user']
            login(request, user)
            return Response(serializer.validated_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)