from django.db import models


# Modelo para la tabla "Formulario"
class Formulario(models.Model):
    nombre = models.CharField(max_length=30)  
    descripcion = models.CharField(max_length=40)  
    fecha_creacion = models.DateField()  

    def __str__(self):
        return self.nombre

# Modelo para la tabla "INFO_FORM"
class InfoForm(models.Model):
    tipo = models.CharField(max_length=20)  
    titulo = models.CharField(max_length=30)  
    opciones = models.CharField(max_length=100)  
    obligatorio = models.BooleanField()  
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE) 

    def __str__(self):
        return self.titulo
