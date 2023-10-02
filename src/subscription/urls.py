from rest_framework.routers import SimpleRouter
from .views import SubscriptionViewSet

router = SimpleRouter()
router.register("", SubscriptionViewSet, basename="subscription")

urlpatterns = router.urls