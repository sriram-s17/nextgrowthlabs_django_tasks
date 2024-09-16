from rest_framework import serializers
from .models import App

class AppSerializer(serializers.ModelSerialzer):
    class Meta:
        model = App
        fields = '__all__'