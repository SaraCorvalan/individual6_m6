from django.db import models

# Create your models here.
class registroClientes(models.Model):
    rut = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=8)
    creacion = models.DateField(auto_now_add=True)
                             
    def __str__(self):
        return "Usuario RUT %s y nombre %s %s" %(self.rut, self.nombre, self.apellido)