from django.urls import include,path
from rest_framework.routers import DefaultRouter
from .views import CategoryModelViewSet, ProductModelViewSet, RatingModelViewSet

router= DefaultRouter()
app_name='product'

router.register(r'category', CategoryModelViewSet, basename='category')
router.register(r'product', ProductModelViewSet, basename='product')
router.register(r'rating', RatingModelViewSet, basename='rating')



urlpatterns=[
    path('', include(router.urls))

]