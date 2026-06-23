from django.urls import path
from .views import (
    ClienteListView,
    ClienteCreateView,
    ClienteUpdateView,
    ClienteDeleteView
)

urlpatterns = [
    path('', ClienteListView.as_view(), name='cliente_list'),
    path('novo/', ClienteCreateView.as_view(), name='cliente_create'),
    path('editar/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('deletar/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_delete'),
]