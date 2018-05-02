from rest_framework import serializers

from .models import Security, Camera


class SecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Security
        fields = "__all__"


class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = "__all__"
