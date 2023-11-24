from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Cart
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def create_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)
        Token.objects.create(user=instance)