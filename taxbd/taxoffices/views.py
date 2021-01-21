from django.shortcuts import render

# Create your views here.

from .models import Zone
from .serializers import ZoneSerializer
from rest_framework import generics

class ZoneList(generics.ListCreateAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer


