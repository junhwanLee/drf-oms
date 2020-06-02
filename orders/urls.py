from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'', OrderViewSet, basename='orders')

urlpatterns = router.urls