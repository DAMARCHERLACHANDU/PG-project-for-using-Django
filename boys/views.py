from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def siva(request):
    return HttpResponse(''' <h1> DAMARCHERLA WENT SIVA PG</h1>
                            <h1> CHANDU WENT SIVA PG</h1>
                           
                        ''')