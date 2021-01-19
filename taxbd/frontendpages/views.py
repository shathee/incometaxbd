from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(*args, **kwargs):
    return HttpResponse("Welcome to Your Tax Home")

def about():
    return HttpResponse("Your Tax About")
    
def contact():
    return HttpResponse("Your Tax Contact")