from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def mainWindow(request):
    return HttpResponse("<a href='http://127.0.0.1:8000/app1_home'> link to registratiLon page </a> <br> <h2> prime intuit is a good finishing school")
