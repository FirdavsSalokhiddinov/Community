from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Visit
from .serializers import VisitSerializer

# Create your views here.
@api_view(["GET"])
def visits(request):
    visits = Visit.objects.all()
    serializer = VisitSerializer(visits, many=True)
    return Response(serializer.data)