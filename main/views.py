from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
	return HttpResponse("<h1>Hello, my name is  Marian!</h1>")

def index2(response):
	return HttpResponse("<h1>I am python developer!</h1>")