from rest_framework.routers import DefaultRouter
from .viewsets import ComentViewSet


router = DefaultRouter()
router.register(r'comments', ComentViewSet)

urlpatterns = router.urls