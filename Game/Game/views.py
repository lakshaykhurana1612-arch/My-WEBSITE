from django.shortcuts import render

def home_view(request):
    return render(request, 'index.html')

def ev_bikes_view(request):
    return render(request, 'ev_bikes.html')  # use underscore
