from django.contrib import admin
from .models import Category, Product, Rating

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Rating)


admin.site.site_header = "Luga Pasal"
admin.site.site_title = "Luga Pasal Admin Portal"
admin.site.index_title = "Welcome to Luga Pasal"