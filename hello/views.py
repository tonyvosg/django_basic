from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "hello/index.html")
def brian(request):
    return HttpResponse('<h1>Hello brian</h1>')
def david(request):
    return HttpResponse('<h1>Hello david</h1>')
def greet(request,name):
    return render(request, "hello/greet.html",{
        "name" : name.capitalize()
    })