from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def welcome(Request):
    # return HttpResponse("<h1 style = 'background:pink'> Hello! all this is my first Django app </h1>")
    my_dict = {'insert_me':"I am coming from view.py file of app1_home/reg.html"
                           ""
                           ""
                           ""}
    return render(Request,'app1_home/reg.html',context = my_dict)