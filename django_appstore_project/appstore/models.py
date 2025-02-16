from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class App(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1024)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="apps")
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
