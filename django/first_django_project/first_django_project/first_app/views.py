from django.shortcuts import redirect, render, HttpResponse

def index(request):
    return HttpResponse("This is my response!")


def create(request):
    return redirect('/')


def show(request, number1):
    return HttpResponse(f"placeholer to display blog number {number1}")

def edit(request, number):
    return HttpResponse(f" placeholder to edit blog {number}")

def destroy(request, number):
    return redirect('/')

# Create your views here.
