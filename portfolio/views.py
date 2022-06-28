from django.shortcuts import render

from .models import Project
# Create your views here.

def home(request):
    #trae todos los projects creados hasta el momento
    projects = Project.objects.all()

    # la clave del diccionario es a eleccion.
    return(render(request, "home.html", {'projects': projects})) 