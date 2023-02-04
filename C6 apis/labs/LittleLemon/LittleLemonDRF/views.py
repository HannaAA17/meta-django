from django.shortcuts import render
from rest_framework import generics

from .models import MenuItem
from .serializers import MenuItemSerializer
# Create your views here.

class MenuItemListView(generics.ListCreateAPIView):
    # its very important to use select_related here
    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemSerializer

class singleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
