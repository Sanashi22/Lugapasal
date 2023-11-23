from rest_framework import serializers
from .models import CartItem, Cart

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model= CartItem
        fields= ('id','product','user','quantity','total_price')

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['carts', 'grand_total']