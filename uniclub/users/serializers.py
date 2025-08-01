from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from . import models
from .models import CustomUser

User = get_user_model()

class UserSerializer (serializers.ModelSerializer):
    class Meta: 
        model = User 
        #fields = ['id','username','email','university','phone','sex','wilaya']  
        fields = '__all__'
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True ) 
    sex = serializers.CharField(write_only = True) # password and sex won't be in the response 
    
    class Meta: 
        model = User 
        # The updated fields list
        fields = [
    'id', 'username', 'email', 'password', 'first_name', 'last_name', 
    'wilaya', 'university', 'phone', 'sex', 
    'bio', 'year_of_study', 'field', 'graduation_year'
    ]
        #fields = '__all__'
    def create(self , validated_data):
        user = User.objects.create_user(**validated_data)  
        return user 




class ProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['profile_picture']

    