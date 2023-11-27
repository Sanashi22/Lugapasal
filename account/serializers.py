from rest_framework import serializers
from django.contrib.auth.models import User
from .validation import validate_is_empty
from rest_framework.validators import UniqueValidator



class UserloginSerializer(serializers.Serializer):
    username= serializers.CharField()
    password= serializers.CharField()

class UserSignUpSerializer(serializers.ModelSerializer):
    first_name=serializers.CharField()
    last_name= serializers.CharField()
    email = serializers.EmailField(validators=[UniqueValidator(
        queryset=User.objects.all (), message='Email Already Exist')])
    class Meta:
        model=User
        fields=('first_name','last_name', 'username','email','password') # import from user
        extra_kwargs={'password':{'write_only': True}} # password will only write

        




    def create(self,validated_data):
        user=User.objects.create(
            first_name= validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            username=validated_data['username']
                )
            
        user.set_password(validated_data['password'])
        user.save()
        return user



    


            

