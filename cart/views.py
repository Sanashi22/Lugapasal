from rest_framework.viewsets import ModelViewSet
from .models import CartItem
from .serializers import CartItemSerializer

# Create your views here.

# class ListCreateCartItemAPIView(ListCreateAPIView):
#     serializer_class= CartItemSerializer

#     def get_queryset(self):
#         qs=CartItem.objects.filter(user=self.request.user)
#         return qs # to get the views for who is sign in
    
class CartModelViewSet(ModelViewSet):
    serializer_class= CartItemSerializer

    def get_queryset(self):
        qs=CartItem.objects.filter(user=self.request.user)
        return qs