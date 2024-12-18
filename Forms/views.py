from django.shortcuts import render, get_object_or_404, redirect
from .models import Formulario, InfoForm



#METODOS PARA MODELO FORMULARIO 
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

        idForm =formulario.id
        # Redirigir a la vista consultarForm después de guardar
        return redirect(f"../editarForm/{idForm}")

    # Si la solicitud es GET, renderizar el formulario en el modal
    return render(request, 'index.html', {'show_modal': True})

def editarForm(request, id):
    # Obtener el objeto a editar, si no existe, devolver 404
    formulario = get_object_or_404(Formulario, id=id)
    
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

#METODO PARA EL MODELO INFOFORM 
#Metodo de crear info form checkbox 
def crearInfoForm1(request, id):
    formularioId = Formulario.objects.get(id=id)

    if request.method == 'POST':
        # Obtener los datos del formulario
        tipo = request.POST.get('tipo')
        titulo = request.POST.get('titulo')
        
        # Obtener las opciones como una lista de valores
        opciones = request.POST.getlist('opciones')  # Esto obtiene todas las opciones seleccionadas

        # Si hay opciones, las unimos en una cadena separada por comas para almacenarlas
        opciones = ",".join(opciones)

        # Crear un nuevo objeto InfoForm con los datos del formulario
        infoForm = InfoForm(tipo=tipo, titulo=titulo, opciones=opciones, idFormulario=formularioId)
        infoForm.save()

        return redirect('editarForm', id=formularioId.id)

    return redirect('editarForm', id=formularioId.id)

#Metodo de crear info form lista
def crearInfoForm2(request, id):
    formularioId = Formulario.objects.get(id=id)

    if request.method == 'POST':
        # Obtener los datos del formulario
        tipo = request.POST.get('tipo')
        titulo = request.POST.get('titulo')
        opciones = request.POST.getlist('opciones')  # Obtiene todos los campos con name="opciones"

        # Filtrar opciones vacías o espacios en blanco
        opciones = [opcion.strip() for opcion in opciones if opcion.strip()]

        # Crear un nuevo objeto InfoForm con los datos del formulario
        infoForm = InfoForm(tipo=tipo, titulo=titulo, opciones=opciones, idFormulario=formularioId)
        infoForm.save()

        return redirect('editarForm', id=formularioId.id)

    return redirect('editarForm', id=formularioId.id)

def consultarInfoForm(request, id):
    infoForm = Formulario.objects.get(id=id)  # Obtener todos los formularios
    return render(request, 'formEditForm.html', {'infoForm': infoForm})  # Pasar los formularios a la plantilla