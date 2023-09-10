from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Reservation
from .serializers import ReservationSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    """These endpoints provide CRUD operations for Reservation model. Only authenticated users can access them. A user can only access their own reservations."""

    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)
