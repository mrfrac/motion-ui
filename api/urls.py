from django.urls import include, path

from rest_framework import viewsets, serializers
from rest_framework.routers import DefaultRouter

from .models import Security


class SecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Security
        fields = '__all__'


class SecurityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Security.objects.all()
    serializer_class = SecuritySerializer


router = DefaultRouter()
router.register('security', SecurityViewSet)
urlpatterns = [
    path('', include(router.urls))
]
