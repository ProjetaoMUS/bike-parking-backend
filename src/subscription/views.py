from django.utils import timezone
from drf_spectacular.utils import extend_schema, inline_serializer

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Subscription
from .serializers import SubscriptionSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    @action(methods=["get"], url_path="is-active", url_name="is-active", detail=False)
    def is_active(self, request):
        """This endpoint returns whether the user has an active subscription."""
        subscriptions = Subscription.objects.filter(
            user=request.user, end_date__gte=timezone.now()
        )
        for subscription in subscriptions:
            if subscription.is_active:
                return Response(self.get_serializer(subscription).data)
        return Response({})
