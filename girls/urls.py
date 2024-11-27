from django.urls import path

from girls.views import *

urlpatterns = [
    path('lakshmi/',lakshmi,name='lakshmi'),
    path('devi/',devi,name='devi'),
]
