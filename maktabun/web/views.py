from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def deshboard(request):
    return render(request, 'home.html')
def home(request):
    return render(request, 'home.html')
def library(request):
    return render(request, 'library.html')
def about(request):
    return render(request, 'about.html')
def contract(request):
    return render(request, 'contract.html')