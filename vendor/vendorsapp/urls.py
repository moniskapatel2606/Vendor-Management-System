from django.urls import path
from .views import *

app_name='vendors'

urlpatterns = [
    path('', index, name='index'),
    
]
