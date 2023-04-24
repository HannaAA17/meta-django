from rest_framework import serializers

from .models import User, MenuItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_superuser', 'groups.name')

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('id', 'title', 'price', 'featured', 'category')