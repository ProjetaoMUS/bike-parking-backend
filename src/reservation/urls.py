from rest_framework.routers import SimpleRouter

from .views import ReservationViewSet

router = SimpleRouter()
router.register("", ReservationViewSet, basename="reservation")

urlpatterns = router.urls
