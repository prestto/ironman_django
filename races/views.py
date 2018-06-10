from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def race_home(request):
	return HttpResponse("this is the races home page!!")
