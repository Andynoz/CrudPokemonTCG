from django.shortcuts import render
from django.http import JsonResponse
from .models import Producto

# Create your views here.
def lista_prodcutos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def detail_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'productos/detalle_producto.html', {'producto': producto})

def buscar_productos(request):
    termino_busqueda = request.GET.get('termino', '')
    productos = Producto.objects.filter(nombre__icontains=termino_busqueda)
    resultados = [{'id': producto.id,'nombre': producto.nombre, 'precio': producto.precio} for producto in productos]
    return JsonResponse({'resultados': resultados})