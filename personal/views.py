from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def personal_website(request):
    return render(request, 'personal/personal.html')

def pretty_website(request):
    return render(request, 'personal/pretty.html')

def pretty_test_site(request):
    return render(request, 'personal/pretty-test.html')

def personal_achievments(request):
    return render(request, 'personal/personal_achievments.html')