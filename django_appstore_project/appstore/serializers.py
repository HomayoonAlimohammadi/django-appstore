from rest_framework import serializers
from .models import App

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ['id', 'title', 'description', 'price', 'owner', 'is_verified', 'created_at', 'updated_at']
        read_only_fields = ('id', 'owner', 'is_verified', 'created_at', 'updated_at')

