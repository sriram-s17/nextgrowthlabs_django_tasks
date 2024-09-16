from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

class UserLogoutView(APIView):
    permission_classes = []
    def post(self, request):
        if 