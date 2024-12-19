# urls.py
from django.urls import path
from . import views

#Urls para el entrada a los metodos 
urlpatterns = [
    path('', views.consultarForm, name='consultarForm'),  # Ruta para la vista que muestra los formularios
    path('crear/', views.crearForm, name='crearForm'),     # Ruta para la vista de creación de formularios
    path('editarForm/<int:id>/', views.editarForm, name='editarForm'), # Ruta para la vista de editar el formulario
    path('eliminarForm/<int:id>/', views.eliminarForm, name='eliminarForm'), #Ruta para eliminar formulario
    path('crearInfoForm1/<int:id>/', views.crearInfoForm1, name='crearInfoForm1'), #Ruta para crear componente
    path('crearInfoForm2/<int:id>/', views.crearInfoForm2, name='crearInfoForm2'), #Ruta para crear componente lista
    path('eliminarInfoForm/<int:id>/', views.eliminarInfoForm, name='eliminarInfoForm'), #Ruta para eliminr componente
]
