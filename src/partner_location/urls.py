from rest_framework.routers import SimpleRouter

from .views import LocalViewSet

router = SimpleRouter()
router.register("", LocalViewSet, basename="partner_location")

urlpatterns = router.urls
