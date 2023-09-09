from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import CustomUser
from .permissions import IsUserOrReadOnly
from .serializers import CustomUserSerializer


class CustomUserViewSet(ModelViewSet):
    """Viewset for the CustomUser model."""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    permission_classes = [IsUserOrReadOnly]
