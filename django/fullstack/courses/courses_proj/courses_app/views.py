from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages
# Create your views here.

def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, 'index.html', context)

def create(request):


    errors = Course.objects.basic_validator(request.POST)

    if len(errors)>0:
        for key,val in errors.items():
            messages.error(request, val)
        return redirect('/')
    
    Course.objects.create(
        name = request.POST['name'],
        description = request.POST['description'],
        
        
    )

    return redirect('/')

def destroy(request, course_id):

    context={
        "course": Course.objects.get(id=course_id)
    }

    return render(request, 'destroy.html', context)

def remove(request, course_id):
    deleted_course = Course.objects.get(id=course_id)
    deleted_course.delete()
    return redirect('/')
