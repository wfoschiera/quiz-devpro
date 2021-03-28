from django.shortcuts import render

# Create your views here.
from quiz.base.models import Pergunta


def home(request):
    return render(request, 'base/home.html')


def perguntas(request, indice):
    pergunta = Pergunta.objects.filter(disponivel=True).order_by('id')[indice - 1]
    ctx = { 'indice_da_questao': indice, 'pergunta': pergunta }
    return render(request, 'base/game.html', context=ctx)


def classificacao(request):
    return render(request, 'base/classificacao.html')