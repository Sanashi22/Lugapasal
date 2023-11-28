from rest_framework.routers import DefaultRouter
from .views import OrderItemViewSet, OrderViewSet
 
router = DefaultRouter()
 
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'order-item', OrderItemViewSet, basename='order-item')
 
app_name = "order"
 
urlpatterns = router.urls