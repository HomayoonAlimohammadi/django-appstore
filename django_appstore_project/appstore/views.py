from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import App
from .serializers import AppSerializer

class AppCreateAPIView(generics.CreateAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically assign the authenticated user as the owner
        serializer.save(owner=self.request.user)

class SignupAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return Response({"message": "Signup endpoint is under construction."})

class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return Response({"message": "Login endpoint is under construction."})

class AppListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"message": "App listing endpoint is under construction."})

class PurchaseAPIView(APIView):
    def post(self, request, *args, **kwargs):
        return Response({"message": "Purchase endpoint is under construction."})
