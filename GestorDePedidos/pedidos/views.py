from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render
from .models import Pedido

# Create your views here.
def index(request):
    return render(request, "pedidos/index.html", {
        "pedidos": Pedido.objects.all()
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