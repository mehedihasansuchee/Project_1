from django.shortcuts import render
from django.http import HttpResponse
from web.models import Contract

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
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')

        # Save to database
        Contract.objects.create(name=name, email=email, desc=desc)

        # Send success flag to template
        return render(request, 'contract.html', {"success": True})

    return render(request, 'contract.html')