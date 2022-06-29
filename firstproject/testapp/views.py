from re import S
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
   print(type(request))
   print('Hello')
   s='<h1>Dont feel difficult... Really django is very easy</h1>'
   return HttpResponse(s)