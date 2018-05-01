from json import dumps

from django.contrib.auth import login
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class MyBasicAuthentication(BasicAuthentication):

    def authenticate(self, request):
        user, _ = super(MyBasicAuthentication, self).authenticate(request)
        if user:
            login(request, user)
        return user, _


class ExampleView(APIView):
    authentication_classes = (SessionAuthentication, MyBasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'user': request.user.username,
            'auth': request.auth,  # None
        }
        return Response(dumps(content))
