from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.

def index(request):


    context={
        "dojos": Dojo.objects.all(),
        "ninjas":Ninja.objects.all()
    }

    return render(request, 'index.html', context)


def create_dojo(request):
  
    Dojo.objects.create(
        name = request.POST['dojo_name'],
        city = request.POST['dojo_city'],
        state = request.POST['dojo_state']
    )
    return redirect('/')

def create_ninja(request):
  
    Ninja.objects.create(
        first_name = request.POST['ninja_first_name'],
        last_name = request.POST['ninja_last_name'],
        dojo_id = request.POST['assigned_dojo']    #??????
    )
    return redirect('/')
