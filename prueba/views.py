from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'prueba/index.html ' ,{})

def about(request):
    return render(request, 'prueba/about.html' ,{})

def sample(request):
    return render(request, 'prueba/sample.html' ,{})

def store(request):
    return render(request, 'prueba/store.html' ,{})
