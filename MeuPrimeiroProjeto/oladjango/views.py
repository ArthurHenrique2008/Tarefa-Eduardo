from django.http import HttpResponse
from django.shortcuts import render, redirect


from oladjango.models import Categorias


# Create your views here.



def olamundo(request):
    return HttpResponse('Ola Mundo')


# Mostra todo o conteúdo
def paginaInicial(request):
    listaDeCategorias = Categorias.objects.all()
    context = {"listaDeCategorias":  listaDeCategorias}

    return render(request, "base.html", context)


def editar(request, catid):

    categoria = Categorias.objects.get(pk=catid)

    context = {"categoria": categoria}
    return render(request, "editarcategoria.html", context)

from .forms import *
def editar2(request, catid):
    categoria = Categorias.objects.get(pk=catid)
    formcategoria = FormCategorias(instance=categoria)

    context = {"categoriaform": formcategoria }

    return render(request, "editarcategoria2.html", context)

def editarcategoria(request):
    if request.method == "POST":
        categoria = Categorias.objects.get(pk=request.POST["id"])
        categoria.nome = request.POST["nome"]
        categoria.save()
        return redirect("/")
    else:
        return HttpResponse("Nenhum dado foi passado na requisição")


def remover(request, catid):
    registroremover = Categorias.objects.get(pk=catid)
    registroremover.delete()
    return redirect("/")

def adicionar(request):
    if request.method == "POST":
        categoria = Categorias()
        categoria.nome = request.POST["nome"]
        categoria.save()
        return redirect("/")
    else:
        return render(request, "adicionarcategoria.html")


def adicionarform(request):
    return render(request, "adicionarcategoria.html")






# starta a aplicação
# python manage.py runserver

