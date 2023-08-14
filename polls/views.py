from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bem vindo ao site oficial de Victor, Pagina Principal.")

