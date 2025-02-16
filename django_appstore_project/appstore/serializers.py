from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import App

User = get_user_model()

class AppSerializer(serializers.ModelSerializer):
    """
    Serializer for the App model.
    """
    class Meta:
        """
        Metadata for the AppSerializer.
        """
        model = App
        fields = ['id', 'title', 'description', 'price', 'owner', 'is_verified', 'created_at', 'updated_at']
        read_only_fields = ('id', 'owner', 'is_verified', 'created_at', 'updated_at')

class UserSignupSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    """
    password = serializers.CharField(write_only=True, help_text="Password for the new user.")

    class Meta:
        """
        Metadata for the UserSignupSerializer.
        """
        model = User
        fields = ('id', 'username', 'email', 'password')
    
    def create(self, validated_data):
        """
        Create a new user with encrypted password.
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    """
    username = serializers.CharField(help_text="Username of the user")
    password = serializers.CharField(write_only=True, help_text="Password of the user")
