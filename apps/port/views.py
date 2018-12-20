from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render (request, 'portfolio/index.html')

def travel_itineraries(request):
    return render (request, 'portfolio/travel_itineraries.html')

def skin_deep(request):
    return render (request, 'portfolio/skin_deep.html')

def handy_helper(request):
    return render (request, 'portfolio/handy_helper.html')

def restaurant_reviewer(request):
    return render (request, 'portfolio/restaurant_reviewer.html')

def courses(request):
    return render (request, 'portfolio/courses.html')

def justyoufitness(request):
    return render (request, 'portfolio/just_you.html')