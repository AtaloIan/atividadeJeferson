from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def dados_pessoais(request):
    return render(request, 'dados_pessoais.html')

def cursos(request):
    return render(request, 'cursos.html')

def interesses(request):
    return render(request, 'interesses.html')