from django.urls import path
from . import views

urlpatterns = [
    # generic views
    path('g/menu-items', views.MenuItemListView.as_view()),
    path('g/menu-items/<int:pk>', views.singleMenuItemView.as_view()),
    path('g/category', views.CategoriesView.as_view()),
    
    # viewsets
    path('menu-items', views.MenuItemViewSet.as_view({'get': 'list'})),
    path('menu-items/<int:pk>', views.MenuItemViewSet.as_view({'get': 'retrieve'})),
]