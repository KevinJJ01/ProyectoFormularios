from django.db import models


class Formulario(models.Model):
    Nombre = models.CharField(max_length=30)
    Descripcion = models.CharField(max_length=40)
    Fecha_Creacion = models.DateField(auto_now_add=True)  # Asignar la fecha actual automáticamente
     
    def __str__(self):
        return self.Nombre

# Modelo para la tabla "INFO_FORM"
class InfoForm(models.Model):
    tipo = models.CharField(max_length=20)  
    titulo = models.CharField(max_length=30)  
    opciones = models.CharField(max_length=100)  
    obligatorio = models.BooleanField()  
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE) 

    def __str__(self):
        return self.titulo
