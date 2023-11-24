from rest_framework.routers import DefaultRouter
from .viewsets import *


router = DefaultRouter()
router.register(r'reactions', 0)

urlpatterns = router.urls