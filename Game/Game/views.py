#I have created it
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'Ev bikes.html')

def About(request):
   return HttpResponse (" What about you")
