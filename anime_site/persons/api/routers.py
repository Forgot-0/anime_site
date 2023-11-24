from rest_framework.routers import DefaultRouter
from .viewsets import PersonViewSet


router = DefaultRouter()
router.register(r'persons', PersonViewSet)

urlpatterns = router.urls