from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .models import App
from .serializers import AppSerializer

# this class is for getting list of added apps and adding new app details.
class AppListCreateView(APIView):
    permission_classes = [IsAdminUser]

    # get method for getting all apps details
    def get(self, request):
        apps = App.objects.all()
        serializer = AppSerializer(apps, many=True)
        return Response(serializer.data)
    
    # post method for adding new app details
    def post(self, request):
        serializer = AppSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)