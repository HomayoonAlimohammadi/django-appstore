from django.urls import path
from .views import AppCreateAPIView

urlpatterns = [
    path('apps/create/', AppCreateAPIView.as_view(), name='app-create'),
]

