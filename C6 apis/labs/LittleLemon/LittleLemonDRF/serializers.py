from rest_framework import serializers

from .models import Menuitem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menuitem
        fields = ('id', 'title', 'price', 'inventory')
        extra_kwargs = {
            'price': {'min_value':2},
            'inventory': {'min_value':0},
        }
