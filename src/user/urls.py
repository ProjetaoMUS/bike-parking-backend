from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import CustomUserViewSet

router = SimpleRouter()
router.register("", CustomUserViewSet, basename="user")

urlpatterns = router.urls
