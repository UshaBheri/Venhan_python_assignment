from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sayHelloWorld(request):
    return HttpResponse('<h1 style="color: blue">Hello, World!</h1>')
