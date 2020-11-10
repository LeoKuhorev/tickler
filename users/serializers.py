from rest_framework import serializers
from .models import CustomUser, Profile


class ProfileSerializer(serializers.ModelSerializer):
    is_manager = serializers.CharField(source="user.is_staff", read_only=True)
    class Meta:
        fields = ('phone_number', 'allow_notifications', "is_manager")
        model = Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email',)
        model = CustomUser