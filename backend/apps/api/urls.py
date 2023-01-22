from rest_framework.routers import DefaultRouter
from apps.api import views

router = DefaultRouter()

router.register('cards', views.CardAPIViewSet, basename='cards')
router.register('products', views.ProductAPIViewSet, basename='product')
router.register('orders', views.OrderAPIViewSet, basename='order')

urlpatterns = router.urls
