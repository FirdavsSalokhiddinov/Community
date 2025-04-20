from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Event, Club
from .serializers import EventSerializer, ClubSerializer

@api_view(['GET'])
def events(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def clubs(request):
    clubs = Club.objects.all()
    serializer = ClubSerializer(clubs, many=True)
    return Response(serializer.data)