from django.urls import path
from .views import ThingsListView, ThingsDetailView, ThingsCreateView, ThingsUpdateView, ThingsDeleteView

urlpatterns = [
    path('', ThingsListView.as_view(), name='_list'),
    path('<int:pk>/', ThingsDetailView.as_view(), name='_detail'),
    path('create/', ThingsCreateView.as_view(), name='_create'),
    path('<int:pk>/update/', ThingsUpdateView.as_view(), name='_update'),
    path('<int:pk>/delete/', ThingsDeleteView.as_view(), name='_delete'),
]