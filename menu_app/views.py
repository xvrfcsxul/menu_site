from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    if request.method == 'GET': 
        return render(request, 'menu_app/index.html')

def view_2(request):
    if request.method == 'GET':
        return render(request, 'menu_app/index.html')

def view_3(request):
    if request.method == 'GET':
        return render(request, 'menu_app/index.html')

def view_4(request):
    if request.method == 'GET':
        return render(request, 'menu_app/index.html')

def view_5(request):
    if request.method == 'GET':
        return render(request, 'menu_app/index.html')

def view_6(request):
    if request.method == 'GET':
        return render(request, 'menu_app/index.html')