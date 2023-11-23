from rest_framework.viewsets import ModelViewSet
from .models import CartItem, Cart
from .serializers import CartItemSerializer, CartSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class CartItemModelViewSet(ModelViewSet):
    serializer_class= CartItemSerializer

    def get_queryset(self):
        qs=CartItem.objects.filter(user=self.request.user)
        return qs # to get the views for who is sign in
    
class CartModelViewSet(ModelViewSet):
    serializer_class= CartSerializer

    def get_queryset(self):
        qs=Cart.objects.filter(user=self.request.user)
        return qs
    
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
        # print('data ->', serializer.data.get('user'))
        # serializer.data.get('user').value= self.request.user
        # print('data after update ->', serializer.data.get('user'))
        # self.perform_create(serializer)

        # cart_dict= {}
        # cart_dict.update(serializer.data)
        # cart_dict['user']= self.request.user.id
        # print('cart dict->', cart_dict)
        # self.perform_create(cart_dict)
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
       