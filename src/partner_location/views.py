from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import PartnerLocation
from .serializers import PartnerLocationSerializer

class LocalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PartnerLocation.objects.all()
    serializer_class = PartnerLocationSerializer