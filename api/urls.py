from django.utils import timezone
from django.urls import include, path
from rest_framework import viewsets, serializers
from rest_framework.routers import DefaultRouter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Security


class SecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Security
        fields = "__all__"


class SecurityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Security.objects.all()
    serializer_class = SecuritySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ("camera", )

    def get_queryset(self):
        filters = {}
        queryset = Security.objects.all()
        timestamp = self.request.query_params.get("timestamp_date")

        if timestamp:
            filters["timestamp__date"] = timezone.datetime.strptime(timestamp, "%Y-%m-%d").date()

        if len(filters) > 0:
            return queryset.filter(**filters)

        return queryset


router = DefaultRouter()
router.register('security', SecurityViewSet)
urlpatterns = [
    path('', include(router.urls))
]
