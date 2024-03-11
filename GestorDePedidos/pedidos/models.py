from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.nombre} ({self.direccion})"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre}"

class Pedido(models.Model):
    OPCIONES_DE_ESTADO = (
        ('no_retirado', 'No retirado'),
        ('en_transito', 'En tránsito'),
        ('entregado', 'Entregado'),
        ('cancelado', 'cancelado'),
    )
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    estado = models.CharField(max_length = 24, choices = OPCIONES_DE_ESTADO, default='no_retirado')
    productos = models.ManyToManyField(Producto)
    
    def calcular_precio_total(self):
        return sum(producto.precio for producto in self.productos.all())

    @property
    def precio_total(self):
        return self.calcular_precio_total()
    
    def __str__(self):
        return f"Pedido de {self.cliente.nombre} - {self.cliente.direccion} ({self.cliente.telefono}) - Precio Total: {self.precio_total} - Estado: {self.estado}"