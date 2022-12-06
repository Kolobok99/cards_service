from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.api.views import CardListAndDestroyAPIView, CardGenerator, CardActivateOrDeactivate

# router = DefaultRouter()

# router.register('card', CardViewSet, basename='card')

# urlpatterns = router.urls

urlpatterns = [
    path('card/generation/', CardGenerator.as_view()),
    path('card/activation/<str:number>/', CardActivateOrDeactivate.as_view()),
    path('card/', CardListAndDestroyAPIView.as_view()),
    path('card/<str:number>/', CardListAndDestroyAPIView.as_view()),
]