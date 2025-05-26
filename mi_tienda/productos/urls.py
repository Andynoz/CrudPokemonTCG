from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_prodcutos, name='lista_productos'),
    path('producto/<int:producto_id>/', views.detail_producto, name='detalle_producto'),
    path('buscar/', views.buscar_productos, name='buscar_productos'),
]