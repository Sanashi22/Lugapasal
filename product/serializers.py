from rest_framework import serializers
from .models import Category, Product, Rating
from django.core.exceptions import ValidationError

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('name',)

class ProductSerializer(serializers.ModelSerializer):
    slug=serializers.SlugField(read_only=True)
    class Meta:
        model= Product
        fields= ('name','category','price','description','slug',
                  'image', 'created','updated','avg_rating', 'category_name','quantity', 'stock')
        
    def validate_price(self, price):
        if price <= 0:
            raise ValidationError("Price should be greater than zero.")
        return price
        

class RatingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Rating
        fields= "__all__"

def validate_rating(self, rating):
        if rating not in range(1, 6):
            raise ValidationError(
                "Rating Should be in range 1 to 5 inclusive.")
        return rating