from django.utils import timezone
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Security, Camera
from .serializers import SecuritySerializer, CameraSerializer


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
            dt = timezone.datetime.strptime(timestamp, "%Y-%m-%d").date()
            filters["timestamp__range"] = (timezone.datetime(dt.year, dt.month, dt.day, 0, 0, 0),
                                           timezone.datetime(dt.year, dt.month, dt.day, 23, 59, 59))

        if len(filters) > 0:
            return queryset.filter(**filters)

        return queryset


class CameraViewSet(viewsets.ModelViewSet):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer
