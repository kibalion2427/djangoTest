from django.shortcuts import render
from django.shortcuts import HttpResponse

def Home(request):
    return HttpResponse("<h1>Home view</h1>")

def News(request):
    return HttpResponse("<h1>News view</h1>")