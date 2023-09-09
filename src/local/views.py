from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Local
from .serializers import LocalSerializer

class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer