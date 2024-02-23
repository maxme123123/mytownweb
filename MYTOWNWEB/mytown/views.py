from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def workerlogin(request):
#     return render(request , 'mytown/workerlogin.html')
def workerlogin (request):
    return render(request , 'workerlogin.html')

def addreports (request):
    return render(request , 'addreports.html')
