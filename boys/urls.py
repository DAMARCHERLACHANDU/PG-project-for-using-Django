from django.urls import path

from boys.views import *

urlpatterns = [
    path('siva/',siva,name='siva')
]
