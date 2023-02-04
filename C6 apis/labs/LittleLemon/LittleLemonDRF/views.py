from django.shortcuts import render
from rest_framework import generics, viewsets

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

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'inventory']
    search_fields = ['title', 'category__title']