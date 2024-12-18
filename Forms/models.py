from django.db import models


class Formulario(models.Model):
    Nombre = models.CharField(max_length=30)
    Descripcion = models.CharField(max_length=40)
    FechaCreacion = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.Nombre

# Modelo para la tabla "INFO_FORM"
class InfoForm(models.Model):
    tipo = models.CharField(max_length=20)  
    titulo = models.CharField(max_length=30)  
    opciones = models.TextField(blank=True)
    idFormulario = models.ForeignKey(Formulario, on_delete=models.CASCADE) 

    def get_opciones(self):
        # Convertir la cadena de texto a una lista
        return self.opciones.split(',') if self.opciones else []

    def set_opciones(self, opciones_list):
        # Convertir la lista de nuevo a una cadena separada por comas
        self.opciones = ','.join(opciones_list)

    def __str__(self):
        return self.titulo
