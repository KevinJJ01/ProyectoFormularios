from django.shortcuts import render, get_object_or_404, redirect
from .models import Formulario, InfoForm
import Forms



#METODOS PARA MODELO FORMULARIO 

#Metodo para consultar la lista de formularios principal
def consultarForm(request):
    print(f"Metodo de consulta de Formularios Inicializado")
    formularios = Formulario.objects.all()  # Obtener todos los formularios
    return render(request, 'index.html', {'formularios': formularios})  # Pasar los formularios a la plantilla

#Metodo para la creación de formularios
def crearForm(request):
    print("Metodo de crear Formulario Inicializado")
    if request.method == 'POST':
        # Obtener los datos del formulario de HTML con request.POST.get()
        Nombre = request.POST.get('Nombre')
        Descripcion = request.POST.get('Descripcion')
        # Crear un nuevo objeto Formulario con los datos del formulario
        formulario = Formulario(Nombre=Nombre, Descripcion=Descripcion)
        formulario.save()
        print(f"Formulario guardado: ", formulario)
        idForm =formulario.id
        # Redirigir a la vista consultarForm después de guardar
        return redirect(f"../editarForm/{idForm}")

    # Si la solicitud es GET, renderizar el formulario en el modal
    return render(request, 'index.html', {'show_modal': True})

#Metodo para la edicion de formularios (Y componentes)
def editarForm(request, id):
    print("Metodo de editar Formulario o componente Inicializado")
    # Obtener el formulario principal
    formulario = get_object_or_404(Formulario, id=id)

    # Actualización del formulario principal
    if request.method == 'POST' and 'updateFormulario' in request.POST:
        print("Se editara un Formulario principal")
        Nombre = request.POST.get('Nombre')
        Descripcion = request.POST.get('Descripcion')
        formulario.Nombre = Nombre
        formulario.Descripcion = Descripcion
        formulario.save()
        print(f"Formulario con cambios: ", formulario, " Guardado ")


    # Obtener los InfoForms relacionados
    infoForms = InfoForm.objects.filter(idFormulario=formulario)

    # Convertir opciones en listas para el renderizado
    for infoForm in infoForms:
        infoForm.opciones = infoForm.get_opciones()

    # Actualización de un InfoForm específico
    if request.method == 'POST' and 'updateInfoForm' in request.POST:
        print("Se editara una informacion del Formulario principal")

        # Obtener el ID del InfoForm desde el formulario
        infoForm_id = request.POST.get('infoForm_id')
        infoForm = get_object_or_404(InfoForm, id=infoForm_id)

        # Actualizar los datos del InfoForm
        titulo = request.POST.get('titulo')
        opciones = request.POST.getlist('opciones')  # Lista de opciones

        infoForm.titulo = titulo
        infoForm.set_opciones(opciones)  # Guardar opciones como cadena separada por comas
        infoForm.save()
        print(f"Informacion del Formulario con cambios: ", infoForm, " Guardado ")
        # Redirigir a la misma vista para recargar la información actualizada
        return redirect('editarForm', id=formulario.id)

    print("Proceso de editar formulario finalizado")
    return render(request, 'formEditForm.html', {
        'formulario': formulario,
        'infoForms': infoForms
    })

#Metodo para eliminar formularios
def eliminarForm(request, id):
    # Obtener el objeto a eliminar, si no existe, devolver 404
    objeto = get_object_or_404(Formulario, id=id)
    print(f"Objeto a eliminar ", objeto)
    if request.method == 'GET':
        objeto.delete()  # Eliminar el objeto de la base de datos
        print("Objeto eliminado")
        return redirect('consultarForm')  # Redirigir a la vista consultarForm después de eliminar
    print("Metodo de eliminar Form no es de metodo get, redirigido a metodo consultarForm")
    return redirect('consultarForm')

#Metodo para crear la informacion del formulario (Radio-button y campo de texto)
def crearInfoForm1(request, id):
    formularioId = Formulario.objects.get(id=id) #Se obtiene el id del formulario principal 
    print("Metodo de crearInfoForm1 Inicializado ")

    if request.method == 'POST':
        print("Crear informacion de formulario metodo POST")
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
        print(f"Objeto InfoForm creado: ", infoForm)
        return redirect('editarForm', id=formularioId.id)
    print("Metodo de crear InfoForm no es de metodo get, redirigido a metodo editar Form")
    return redirect('editarForm', id=formularioId.id)

#Metodo para crear la informacion del formulario (Lista desplegable)
def crearInfoForm2(request, id):
    formularioId = Formulario.objects.get(id=id)

    if request.method == 'POST':
        # Obtener los datos del formulario
        tipo = request.POST.get('tipo')
        titulo = request.POST.get('titulo')
        
        # Obtener las opciones como una lista de valores
        opciones = request.POST.getlist('opciones')  # Esto obtiene todas las opciones seleccionadas
        print(f"Opciones recibidas (getlist):", opciones)

        # Crear un nuevo objeto InfoForm con los datos del formulario
        infoForm = InfoForm(tipo=tipo, titulo=titulo, opciones=opciones, idFormulario=formularioId)
        infoForm.save()

        print(f"Objeto InfoForm creado:", infoForm)

        return redirect('editarForm', id=formularioId.id)

    return redirect('editarForm', id=formularioId.id)

#Metodo para eliminar la informacion del formulario
def eliminarInfoForm(request, id ):
    print(f"Metodo para eliminar informacion del formulario Inicializado " )
    # Obtener el objeto a eliminar, si no existe, devolver 404
    objeto = get_object_or_404(InfoForm, id=id)
    idFormulario = objeto.idFormulario.id
    print(f"ID a eliminar: ", idFormulario)
    if request.method == 'GET':
        objeto.delete()  # Eliminar el objeto de la base de datos
        print("Objeto eliminado")
        return redirect('editarForm', idFormulario)  # Redirigir a la vista consultarForm después de eliminar
    print("El metodo de entrada de la solicitud no es GET, redirigido a metodo editar Form")
    return redirect('editarForm', idFormulario )
