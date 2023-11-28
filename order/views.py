from rest_framework.viewsets import ModelViewSet
from .serializers import OrderItemSerializer, OrderSerializer, CreateOrderSerializer
from .models import Order, OrderItem
from rest_framework.filters import SearchFilter
 
 
class OrderItemViewSet(ModelViewSet):
    
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        qs=OrderItem.objects.filter(order__user=self.request.user)
        return qs
 
 
class OrderViewSet(ModelViewSet):
   filter_backends=[SearchFilter]
   search_fields= ['tracking_number']
   def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateOrderSerializer
        return OrderSerializer
   
   def get_serializer_context(self):
        return {'user': self.request.user}
   
   def get_queryset(self):
        qs=Order.objects.filter(user=self.request.user)
        return qs