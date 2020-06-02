from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet, basename='users')

urlpatterns = router.urls
