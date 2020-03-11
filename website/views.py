from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'website/home.html', {})

def addition(request):
    return render(request, 'website/addition.html', {})


def subtraction(request):
    return render(request, 'website/subtraction.html', {})

def multiplications(request):
    return render(request, 'website/multiplications.html', {})

def division(request):
    return render(request, 'website/division.html', {})

