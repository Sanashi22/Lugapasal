from rest_framework.viewsets import ModelViewSet
from .models import Category, Product, Rating
from .serializers import CategorySerializer, ProductSerializer, RatingSerializer

# Create your views here.

class CategoryModelViewSet(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class= CategorySerializer

class ProductModelViewSet(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class= ProductSerializer

class RatingModelViewSet(ModelViewSet):
    queryset=Rating.objects.all()
    serializer_class= RatingSerializer
