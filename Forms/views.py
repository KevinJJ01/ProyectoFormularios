from django.shortcuts import render, get_object_or_404, redirect
from .models import Formulario, InfoForm
import Forms



#METODOS PARA MODELO FORMULARIO 
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
    # Obtener el formulario principal
    formulario = get_object_or_404(Formulario, id=id)

    # Actualización del formulario principal
    if request.method == 'POST' and 'updateFormulario' in request.POST:
        Nombre = request.POST.get('Nombre')
        Descripcion = request.POST.get('Descripcion')

        formulario.Nombre = Nombre
        formulario.Descripcion = Descripcion
        formulario.save()

    # Obtener los InfoForms relacionados
    infoForms = InfoForm.objects.filter(idFormulario=formulario)

    # Convertir opciones en listas para el renderizado
    for infoForm in infoForms:
        infoForm.opciones = infoForm.get_opciones()

    # Actualización de un InfoForm específico
    if request.method == 'POST' and 'updateInfoForm' in request.POST:
        # Obtener el ID del InfoForm desde el formulario
        infoForm_id = request.POST.get('infoForm_id')
        infoForm = get_object_or_404(InfoForm, id=infoForm_id)

        # Actualizar los datos del InfoForm
        titulo = request.POST.get('titulo')
        opciones = request.POST.getlist('opciones')  # Lista de opciones

        infoForm.titulo = titulo
        infoForm.set_opciones(opciones)  # Guardar opciones como cadena separada por comas
        infoForm.save()

        # Redirigir a la misma vista para recargar la información actualizada
        return redirect('editarForm', id=formulario.id)

    return render(request, 'formEditForm.html', {
        'formulario': formulario,
        'infoForms': infoForms
    })

def eliminarForm(request, id):
    # Obtener el objeto a eliminar, si no existe, devolver 404
    objeto = get_object_or_404(Formulario, id=id)
    
    if request.method == 'GET':
        objeto.delete()  # Eliminar el objeto de la base de datos
        print("Objeto eliminado")
        return redirect('consultarForm')  # Redirigir a la vista consultarForm después de eliminar
    return redirect('consultarForm')

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

def crearInfoForm2(request, id):
    formularioId = Formulario.objects.get(id=id)

    if request.method == 'POST':
        # Obtener los datos del formulario
        tipo = request.POST.get('tipo')
        titulo = request.POST.get('titulo')
        
        # Obtener las opciones como una lista de valores
        opciones = request.POST.getlist('opciones')  # Esto obtiene todas las opciones seleccionadas

        print(f"Opciones: ", opciones)

        # Crear un nuevo objeto InfoForm con los datos del formulario
        infoForm = InfoForm(tipo=tipo, titulo=titulo, opciones=opciones, idFormulario=formularioId)
        infoForm.save()

        print(f"Opciones: ", opciones, "infoForm: ", infoForm)

        return redirect('editarForm', id=formularioId.id)

    return redirect('editarForm', id=formularioId.id)


def eliminarInfoForm(request, id ):
    # Obtener el objeto a eliminar, si no existe, devolver 404
    objeto = get_object_or_404(InfoForm, id=id)
    idFormulario = objeto.idFormulario.id
    print(f"ID: ", idFormulario)

    if request.method == 'GET':
        objeto.delete()  # Eliminar el objeto de la base de datos
        print("Objeto eliminado")
        return redirect('editarForm', idFormulario)  # Redirigir a la vista consultarForm después de eliminar
    return redirect('editarForm', idFormulario )