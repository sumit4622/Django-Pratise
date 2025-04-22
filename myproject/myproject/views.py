from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("hello, world. you are at sumit home Page.")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("hello, world. this is about oage2")

def contact(request):
    return HttpResponse("hello, this is Second page 3")

def sumit(request):
    return HttpResponse("hello, world. 4 .")