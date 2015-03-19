from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('Rango says hey there world, check out the <a href="/rango/about/">About</a> page')
	
def about(request):
	return HttpResponse("About rango")