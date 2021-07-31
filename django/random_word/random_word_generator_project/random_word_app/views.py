from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):

    print(request.method)



def randomWord(request):

    if 'count' not in request.session:
        request.session['count'] =0
    request.session['count'] +=1
    request.session['word'] = get_random_string(length=14)
    # context = {
    #     'attempt_number':1,
    #     'random_word':"test_word"

    # }
    return render(request, 'index.html')

def reset(request):
    request.session.flush()
    return redirect('/random_word')

# Create your views here.
