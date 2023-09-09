from rest_framework.routers import SimpleRouter
from .views import LocalViewSet

router = SimpleRouter()
router.register('', LocalViewSet, basename='local')

urlpatterns = router.urls
