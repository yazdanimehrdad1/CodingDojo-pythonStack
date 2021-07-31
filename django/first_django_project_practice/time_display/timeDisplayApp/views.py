from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("This is the index page")

def function_one(request, first_name):
    # return HttpResponse("This is my response")
    return HttpResponse(f"Hi {first_name}")
    
def edit(request, test_number, test_string):
    return HttpResponse(f'This is the edit page for {test_number} and {test_string}')

def show(request):
    context={
        "first_name": "Mehrdad",
        "last_name": "yazdani",
        "address":"9815 Jake Lane",

        "list1":["Mehrdad", "Omid", "Borhan", "Mehran"]
    }

    return render(request, 'index.html', context)