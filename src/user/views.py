from drf_spectacular.utils import extend_schema
from knox.auth import TokenAuthentication
from rest_framework.viewsets import ModelViewSet

from .models import CustomUser
from .permissions import IsUserOrReadOnly
from .serializers import CustomUserSerializer


class CustomUserViewSet(ModelViewSet):
    """
    These endpoints allow CRUD operations over the CustomUser model.
    A user can only edit their own data.
    """

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    permission_classes = [IsUserOrReadOnly]
    authentication_classes = [TokenAuthentication]
