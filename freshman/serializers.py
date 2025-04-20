from rest_framework import serializers
from .models import Visit

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ['id', 'title', 'description', 'latitude', 'longtitude', 'photo', 'category', 'opening_time', 'closing_time', 'created_at', 'updated_at']