from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def slvk(request):
    return HttpResponse('''<h1> BOYS ALSO LIVING IN SLVK CO-LIVING PG</h1>
                           <h1> GIRLS ALSO LIVING IN SLVK CO-LIVING PG</h1>
                        ''')