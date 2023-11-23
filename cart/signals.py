from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CartItem, Cart

@receiver (post_save, sender= CartItem)
def add_to_cart(sender, instance, created, *args, **kwargs):
    if created:
        print('instance->','instance')
        Cart.objects.create(carts=instance)
        # Cart.objects.add(instance)