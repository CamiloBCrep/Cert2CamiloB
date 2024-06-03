from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import nuevo_proyecto
# Create your views here.
def home(request):
    title = "inicio"
    data={
        "title":title
    }
    return render(request, 'core/home.html', data)
def login(request):
    title = "Inicio de sesión"

    data = {
        "title":title,
    }
    return render(request, 'registration/login.html',data)
def exit(request):
    logout(request)
    return redirect('home')

def new_proyecto(request):
    if(request.POST):
        #capturar datos desde el formulario
        estudiante = request.POST['txtEstudiante']
        proy = request.POST['txtProyecto']
        tema = request.POST['txtTema']

        #validaciones de reglas de negocio

        #construir y cargar el objeto con los datos del form
        proyecto = nuevo_proyecto(estudiante=estudiante, proy=proy, tema=tema)


        proyecto.save()
    return render(request, 'core/proyecto.html')

def listar_proyectos(request):
    # Obtener todos los proyectos de la base de datos
    data = nuevo_proyecto.objects.all()
    context = {'proyectos': data}
    # Pasar los proyectos al contexto para que estén disponibles en la plantilla
    return render(request, 'core/home.html', context)