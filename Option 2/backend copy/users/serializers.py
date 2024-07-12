# users/serializers.py

from rest_framework import serializers
from .models import User, UserImage
from rest_framework import generics


class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        fields = ["id", "image", "uploaded_at"]


class UserSerializer(serializers.ModelSerializer):
    images = UserImageSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "age",
            "interests",
            "preferences",
            "images",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"], password=validated_data["password"]
        )
        return user
