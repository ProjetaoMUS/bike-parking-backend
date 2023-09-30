from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Subscription
from .serializers import SubscriptionSerializer
from django.utils import timezone

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    @action(detail=True, methods=['get'], url_path='is-active', url_name='is-active')
    def is_active(self, request, pk=None):
        subscription = self.get_object()
        if subscription.is_active():
            return Response({"is_active": True})
        return Response({"is_active": False})
