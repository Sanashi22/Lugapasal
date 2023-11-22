from rest_framework.viewsets import ModelViewSet
from .models import Category, Product, Rating
from .serializers import CategorySerializer, ProductSerializer, RatingSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilterClass
from rest_framework.filters import SearchFilter

# Create your views here.

class CategoryModelViewSet(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class= CategorySerializer

class ProductModelViewSet(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class= ProductSerializer
    filter_backends= [DjangoFilterBackend, SearchFilter]
    search_fields= ['name']
    filterset_fields= ['category', 'name', 'stock','price']
    filterset_class= ProductFilterClass

class RatingModelViewSet(ModelViewSet):
    queryset=Rating.objects.all()
    serializer_class= RatingSerializer
