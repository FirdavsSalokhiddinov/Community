from rest_framework import serializers
from .models import Event, Club

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['title', 'description', 'latitude', 'longtitude', 'category', 'opening_time', 'closing_time', 'created_at', 'updated_at']

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['name', 'description', 'photo', 'category', 'opening_time', 'closing_time', 'created_at', 'updated_at']