from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import App
from .serializers import AppSerializer

class AppCreateAPIView(generics.CreateAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically assign the authenticated user as the owner
        serializer.save(owner=self.request.user)

