from rest_framework.routers import DefaultRouter

from apps.api.views import CardViewSet

router = DefaultRouter()

router.register('card', CardViewSet, basename='card')

urlpatterns = router.urls