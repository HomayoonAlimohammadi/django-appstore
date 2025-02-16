from django.urls import path
from .views import (
    AppCreateAPIView,
    SignupAPIView,
    LoginAPIView,
    AppListAPIView,
    PurchaseAPIView,
)

urlpatterns = [
    path("apps/create/", AppCreateAPIView.as_view(), name="app-create"),
    path("signup/", SignupAPIView.as_view(), name="signup"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("apps/", AppListAPIView.as_view(), name="app-list"),
    path("apps/purchase/", PurchaseAPIView.as_view(), name="purchase"),
]
