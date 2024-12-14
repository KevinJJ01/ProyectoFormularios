from django.shortcuts import render, get_object_or_404, redirect
from .models import Formulario

# Vista para mostrar los formularios
def consultarForm(request):
    formularios = Formulario.objects.all()  # Obtener todos los formularios
    return render(request, 'index.html', {'formularios': formularios})  # Pasar los formularios a la plantilla

def crearForm(request):
    if request.method == 'POST':
        # Obtener los datos del formulario de HTML con request.POST.get()
        Nombre = request.POST.get('Nombre')
        Descripcion = request.POST.get('Descripcion')
        
        # Crear un nuevo objeto Formulario con los datos del formulario
        formulario = Formulario(Nombre=Nombre, Descripcion=Descripcion)
        # Guardar el formulario en la base de datos
        formulario.save()

        # Redirigir a la vista consultarForm después de guardar
        return redirect('consultarForm')

    # Si la solicitud es GET, renderizar la plantilla con el formulario vacío
    return render(request, 'formRegistroForms.html')

def editarForm(request, id):
    # Obtener el objeto a editar, si no existe, devolver 404
    formulario = get_object_or_404(Formulario, id=id)
    print(f"Objeto a editar ", formulario)
    
    # Si la solicitud es POST (cuando se envía el formulario con los datos)
    if request.method == 'POST':
        # Obtener los datos del formulario desde request.POST
        Nombre = request.POST.get('Nombre')
        Descripcion = request.POST.get('Descripcion')

        # Actualizar el objeto con los nuevos datos
        formulario.Nombre = Nombre
        formulario.Descripcion=Descripcion
        formulario.save()  # Guardar los cambios en la base de datos

        # Redirigir a la vista consultarForm después de guardar
        return redirect('consultarForm')  # Ajusta el nombre de la vista de consulta según lo que tengas

    # Si la solicitud es GET, cargar los datos actuales del formulario en el formulario HTML
    return render(request, 'formEditForm.html', {'formulario': formulario})



def eliminarForm(request, id):
    # Obtener el objeto a eliminar, si no existe, devolver 404
    objeto = get_object_or_404(Formulario, id=id)
    
    if request.method == 'GET':
        objeto.delete()  # Eliminar el objeto de la base de datos
        print("Objeto eliminado")
        return redirect('consultarForm')  # Redirigir a la vista consultarForm después de eliminar
    return redirect('consultarForm')
