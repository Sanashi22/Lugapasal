from rest_framework import serializers
from .models import Category, Product, Rating

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('name',)

class ProductSerializer(serializers.ModelSerializer):
    slug=serializers.SlugField(read_only=True)
    class Meta:
        model= Product
        fields= ('name','category','price','description','slug',
                  'image', 'created','updated','avg_rating')
        depth=1

class RatingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Rating
        fields= "__all__"