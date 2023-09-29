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

    def get_queryset(self):
        if self.request.user is not None:
            return CustomUser.objects.filter(id=self.request.user.id)

        return CustomUser.objects.none()

    serializer_class = CustomUserSerializer

    permission_classes = [IsUserOrReadOnly]
    authentication_classes = [TokenAuthentication]
