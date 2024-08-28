from django.db import models
from django.utils import timezone

class Afiliado(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.CharField(max_length=100, default="",unique=True)
    dni= models.CharField(max_length=8, default="" ,unique=True)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} {self.email} {self.dni}"


class Practica(models.Model):
    codigo= models.CharField(max_length=6, unique=True)
    nombre= models.CharField(max_length=50, unique=True)
    autorizada = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.nombre

class Pedido(models.Model):
    afiliado = models.ForeignKey(Afiliado, on_delete=models.CASCADE)
    practica = models.ForeignKey(Practica, on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField(default=timezone.now)
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
    ], default='pendiente')
    razon_rechazo = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"Pedido {self.id} - {self.afiliado} - {self.practica}"



# Create your models here.
