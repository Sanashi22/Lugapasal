from django.contrib import admin
from .models import Category, Product, Rating

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Rating)
