#from django.shortcuts import render
from rest_framework import viewsets
from core.models import TouristSpot
from .serializers import TouristSpotSerializer

class TouristSpotViewSet(viewsets.ModelViewSet):
    queryset = TouristSpot.objects.all()
    serializer_class = TouristSpotSerializer

    