from django.shortcuts import render, redirect
from .models import Alimento


def home(request):
    alimentos = Alimento.objects.all()
    return render(request, "index.html", {"alimentos": alimentos})


def salvar(request):
    vnome = request.POST.get("nome")
    Alimento.objects.create(nome=vnome)
    alimentos = Alimento.objects.all()
    return render(request, "index.html", {"alimentos": alimentos})


def editar(request, id):
    alimento = Alimento.objects.get(id=id)
    return render(request, "update.html", {"alimento": alimento})


def update(request, id):
    vnome = request.POST.get("nome")
    alimento = Alimento.objects.get(id=id)
    alimento.nome = vnome
    alimento.save()
    return redirect(home)


def delete(request, id):
    alimento = Alimento.objects.get(id=id)
    alimento.delete()
    return redirect(home)
