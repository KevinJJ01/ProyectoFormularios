# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.consultarForm, name='consultarForm'),  # Ruta para la vista que muestra los formularios
    path('crear/', views.crearForm, name='crearForm'),     # Ruta para la vista de creación de formularios
    path('editarForm/<int:id>/', views.editarForm, name='editarForm'), # Ruta para la vista de editar el formulario
    path('eliminarForm/<int:id>/', views.eliminarForm, name='eliminarForm' ) #Ruta para eliminar formulario
]
