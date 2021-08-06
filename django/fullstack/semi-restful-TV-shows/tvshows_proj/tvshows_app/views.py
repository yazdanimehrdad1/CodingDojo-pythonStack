from django.shortcuts import render, redirect,HttpResponse
from .models import TVSHOW
from django.contrib import messages
# Create your views here.

def index(request):
    return redirect('/shows')

def shows(request):
    context={
        "shows":TVSHOW.objects.all()
    }
    return render(request, 'show.html', context)


def add_show(request):
    return render(request, 'add.html')

def create(request):
    # we want to add the items from the form to the db
    errors = TVSHOW.objects.basic_validator(request.POST)

    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect('/shows')


    if request.method== "GET":
        redirect('/')

    TVSHOW.objects.create(
        title=request.POST['title'],
        network = request.POST['network'],
        release_date= request.POST['release_date'],
        description = request.POST['description']

    )
    return redirect('/shows')

def edit(request,show_id):
    context={
        "show": TVSHOW.objects.get(id=show_id)
    }
    return render(request, 'edit.html', context)


def show(request,show_id):
    context={
        "show": TVSHOW.objects.get(id=show_id)
    }
    return render(request, 'showInfo.html', context)


def delete(request, show_id):
    delete_show = TVSHOW.objects.get(id=show_id)
    delete_show.delete()

    return redirect('/shows')


def update(request, show_id):
    item_to_update = TVSHOW.objects.get(id=show_id)

    item_to_update.title = request.POST['title']
    item_to_update.network = request.POST['network']
    item_to_update.release_date = request.POST['release_date']
    item_to_update.description = request.POST['description']
    item_to_update.save()

    return redirect('/shows/'+str(show_id))




