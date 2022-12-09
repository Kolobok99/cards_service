from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.api.views import CardListAPIView, CardGenerator, CardActivateOrDeactivate, OrderAPIViewSet, \
    ProductAPIViewSet, CardRetrieveAndDestroyAPIView

router = DefaultRouter()

router.register('products', ProductAPIViewSet, basename='product')
router.register('orders', OrderAPIViewSet, basename='order')



urlpatterns = [
    path('cards/generation/', CardGenerator.as_view()),
    path('cards/activation/<str:number>/', CardActivateOrDeactivate.as_view()),
    path('cards/', CardListAPIView.as_view()),
    path('cards/<str:number>/', CardRetrieveAndDestroyAPIView.as_view()),


]

urlpatterns += router.urls