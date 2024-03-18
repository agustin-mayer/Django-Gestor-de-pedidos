from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Pedido,Producto,Cliente

def index(request):
    return render(request, "pedidos/index.html", {
        "pedidos": Pedido.objects.all().order_by('-id')
    })

def pedido(request, id_pedido):
    try:
        pedido = Pedido.objects.get(id=id_pedido)
        return render(request, "pedidos/pedido.html", {
            "pedido": pedido,
            "productos": pedido.productos.all()
        })
    except Pedido.DoesNotExist:
        return HttpResponseRedirect(reverse("index"))
    
   
def crear_pedido(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        estado = request.POST.get('estado')
        productos_ids = request.POST.getlist('productos')

        if cliente_id:
            try:
                cliente = Cliente.objects.get(pk=cliente_id)
            except ObjectDoesNotExist:
                return HttpResponseRedirect(reverse("crear_pedido"))
        else:
            return HttpResponseRedirect(reverse("crear_pedido"))

        if productos_ids:
            productos = Producto.objects.filter(pk__in=productos_ids)
        else:
            return HttpResponseRedirect(reverse("crear_pedido"))

        pedido = Pedido.objects.create(cliente=cliente, estado=estado)
        pedido.productos.add(*productos)
        return HttpResponseRedirect(reverse("index"))
    
    opciones_estado = Pedido.OPCIONES_DE_ESTADO
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    return render(request, 'pedidos/crear_pedido.html', {'clientes': clientes, 'productos': productos, 'opciones_de_estado':opciones_estado})


def modificar_pedido(request, pedido_id):
    try:
        pedido = Pedido.objects.get(id=pedido_id)
        if request.method == 'POST':
            cliente_id = request.POST.get('cliente')
            estado = request.POST.get('estado')
            productos_ids = request.POST.getlist('productos')

            if cliente_id:
                try:
                    cliente = Cliente.objects.get(pk=cliente_id)
                except ObjectDoesNotExist:
                    return HttpResponseRedirect(reverse("crear_pedido"))
            else:
                return HttpResponseRedirect(reverse("crear_pedido"))
            
            if productos_ids:
                productos = Producto.objects.filter(pk__in=productos_ids)
            else:
                return HttpResponseRedirect(reverse("crear_pedido"))

            pedido.cliente = cliente
            pedido.productos.set(productos_ids)
            pedido.estado = estado
            pedido.save()

            return HttpResponseRedirect(reverse('index'))
        
        else:
            clientes = Cliente.objects.all()
            productos = Producto.objects.all()
            opciones_de_estado = Pedido.OPCIONES_DE_ESTADO
            return render(request, 'pedidos/modificar_pedido.html', {'pedido': pedido, 'clientes': clientes, 'productos': productos, 'opciones_de_estado': opciones_de_estado})
    except Pedido.DoesNotExist:
        return HttpResponseRedirect(reverse('index'))
    
def eliminar_pedido(request, pedido_id):
    try:
        pedido = Pedido.objects.get(id=pedido_id)
    except Pedido.DoesNotExist:
        raise Http404("El pedido no existe.")  # Lanza una excepción Http404 si el pedido no existe
    
    if request.method == 'POST':
        pedido.delete()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, 'pedidos/error.html', {'mensaje': 'Método de solicitud no permitido.'})
    
def crear_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        Cliente.objects.create(nombre=nombre, direccion=direccion, telefono=telefono)
        return HttpResponseRedirect(reverse("crear_pedido"))
    return render(request, 'pedidos/crear_cliente.html')
   