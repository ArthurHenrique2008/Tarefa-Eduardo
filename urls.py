"""
URL configuration for MeuPrimeiroProjeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from oladjango.views import *

## Este é um olá mundo
urlpatterns = [

    path('admin/', admin.site.urls),
    path('olamundo/', olamundo, name='olamundo'),

    # path('', paginaInicial, name='home'),
    path('editar/<int:catid>/', editar, name='editar'),
    path('editar2/<int:catid>/', editar2, name='editar2'),
    path('editarcategoria', editarcategoria, name='editarcategoria'),

    path('excluir/<int:catid>/', remover, name='excluir'),
    path("adicionar", adicionar, name='adicionar'),
    path("adicionarform", adicionarform, name='adicionarform'),

    path('admin/', admin.site.urls),
    path('', include('clientes.urls')),
]

##
# python manage.py runserver