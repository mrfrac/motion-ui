from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter

from .viewsets import SecurityViewSet, CameraViewSet


router = DefaultRouter()
router.register("security", SecurityViewSet)
router.register("camera", CameraViewSet)
urlpatterns = [
    path("", include(router.urls)),
    path("auth/", obtain_jwt_token),
]
