from django.shortcuts import redirect, render
from .models import *
# Create your views here.
def index(request):
    context={
        "dojos": Dojo.objects.all(),
        "ninjas": Ninja.objects.all()
    }
    return render(request, 'index.html',context)

def add_dojo(request):
    if request.method=="GET":
        return redirect('/')
    dojo =Dojo.objects.create(
        name= request.POST['name'],
        city = request.POST['city'],
        state = request.POST['state']
    )
    return redirect('/')

def add_ninja(request):
    if request.method=="GET":
        return redirect('/')
    
    ninja = Ninja.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        # Either one of the following scrips would work. The second one is using 
        # the exsiting models.objects property to reach the id 
        # you can see that in the models.py for the Ninja class we don't have
        # the dojo_id instead we have the dojo itself. 
        
        # dojo = Dojo.objects.get(id= request.POST['dojo'])
        dojo_id = request.POST['dojo']
    )
    return redirect('/')

def delete_dojo(request,dojo_id ):
    dojo_to_delete= Dojo.objects.get(id=dojo_id)
    dojo_to_delete.delete()
    return redirect('/')

