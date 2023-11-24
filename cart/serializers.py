from rest_framework import serializers
from .models import CartItem, Cart
from product.serializers import ProductSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product= ProductSerializer(many=False)
    class Meta:
        model= CartItem
        fields= ('id','product','user','quantity','sub_total')

class CartSerializer(serializers.ModelSerializer):
    cart = CartItemSerializer(many=True, read_only=True)
 
    class Meta:
        model = Cart
        fields = ['id', 'cart', 'total_price']
 
 
class AddtoCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ("product", 'quantity')
       


class UpdateCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('quantity',)