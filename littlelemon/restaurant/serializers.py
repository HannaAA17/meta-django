from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Menu, Booking

class UserSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = User 
        fields = ['url', 'username', 'email', 'groups']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fiels = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fiels = '__all__'
        