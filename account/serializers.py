from rest_framework import serializers
from django.contrib.auth.models import User

class UserloginSerializer(serializers.Serializer):
    username= serializers.CharField()
    password= serializers.CharField()
