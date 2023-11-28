from django.contrib.auth.models import User
from product.models import Product
from django.db import models
 
ORDER_STATUS = (
    ('processing', 'Processing'),
    ('delivered', 'Delivered'),
)
 
 
class Order(models.Model):
    tracking_number = models.CharField(max_length=10, unique=True)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    order_status = models.CharField(
        max_length=10, choices=ORDER_STATUS, default='processing')
    ordered = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
 
    def total_price(self):
        orders = self.orders.all()
        total = 0
        for order in orders:
            total += order.product.price * order.quantity
        return total
 
    def __str__(self):
        return f"Order has been placed for {self.user.username } at {self.updated.strftime('%d/%m/%Y, %H:%M:%S')}"
 
 
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name='order_products', null=True, blank=True)
    quantity = models.IntegerField(default=1)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f"{self.product.name} has been ordered by {self.order.user.username} at {self.created.strftime('%d/%m/%Y, %H:%M:%S')}"