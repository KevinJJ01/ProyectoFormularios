from django.db import models

#Modelo para la tabla "Formulario"
class Formulario(models.Model):
    Nombre = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=40)
    FechaCreacion = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.Nombre

# Modelo para la tabla "INFO_FORM"
class InfoForm(models.Model):
    tipo = models.CharField(max_length=20)  
    titulo = models.CharField(max_length=40)  
    opciones = models.TextField(default=list, blank=True)
    idFormulario = models.ForeignKey(Formulario, on_delete=models.CASCADE, related_name='infoForm') 

    def get_opciones(self):
        #Convierte la cadena de opciones en una lista
        if self.opciones:
            return self.opciones.split(',')
        return self.opciones

    def set_opciones(self, opciones_list):
        #Convierte una lista de opciones en una cadena separada por comas
        if opciones_list:
            self.opciones = ','.join(opciones_list)
        else:
            self.opciones = ''

    def __str__(self):
        return self.titulo
