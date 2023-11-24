from django.db import models
from django.contrib.auth.models import User
from product.models import Product 

# Create your models here.
class BaseModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract=True #it won't make table while migrating

class Cart(BaseModel):
 
    def total_price(self):
        items = self.cart.all()
        total = 0
        for item in items:
            total += item.product.price * item.quantity
        return total
 
    def __str__(self) -> str:
        return f"{self.user.username} cart created."

class CartItem(BaseModel):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE, null= True, related_name='cart')
    product= models.ForeignKey(Product,on_delete=models.CASCADE, related_name='cart_product')
    quantity= models.PositiveBigIntegerField(default=1)

    def __str__(self):
        return f'{self.product.name} is added to cart.'
    
    def sub_total(self):
        total=self.product.price* self.quantity
        return total
    
    
    

