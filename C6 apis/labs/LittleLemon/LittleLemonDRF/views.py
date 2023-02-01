from django.shortcuts import render
from rest_framework import generics

from .models import Menuitem
from .serializers import MenuItemSerializer
# Create your views here.

class MenuItemListView(generics.ListCreateAPIView):
    queryset = Menuitem.objects.all()
    serializer_class = MenuItemSerializer

class singleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menuitem.objects.all()
    serializer_class = MenuItemSerializer
