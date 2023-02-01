from django.urls import path
from . import views

urlpatterns = [
    path('menu-items', views.MenuItemListView.as_view()),
    path('menu-items/<int:pk>', views.singleMenuItemView.as_view()),
]