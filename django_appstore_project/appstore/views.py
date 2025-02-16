from typing import Any
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from .models import App
from .serializers import (
    AppSerializer,
    UserSignupSerializer,
    LoginSerializer,
)


class AppCreateAPIView(generics.CreateAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SignupAPIView(generics.CreateAPIView):
    """
    API view for user registration.
    """

    serializer_class = UserSignupSerializer
    permission_classes = [AllowAny]


class LoginAPIView(generics.GenericAPIView):
    """
    API view for user login using DRF generics.
    """

    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        """
        Validate credentials and return an authentication token if valid.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data["username"], password=serializer.validated_data["password"]
        )
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})


class AppListAPIView(generics.ListAPIView):
    """
    API view to list all apps.
    """

    queryset = App.objects.all()
    serializer_class = AppSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class PurchaseAPIView(APIView):
    def post(self, request, *args, **kwargs):
        return Response({"message": "Purchase endpoint is under construction."})
