from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def lakshmi(request):
    return HttpResponse('<h1> JYO WENT LAKSHMI PG</h1>')

def devi(request):
    return HttpResponse('<h1> GUNTI WENT DEVI PG</h1>')