from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def personal_website(request):
    return render(request, 'personal/personal.html')

def pretty_website(request):
    return render(request, 'personal/pretty.html')