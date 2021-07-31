from django.shortcuts import render,redirect, HttpResponse
import random , pytz
from datetime import datetime
from pytz import timezone 

def index(request):

    if 'gold' not in request.session or 'activities' not in request.session:
        request.session['gold'] =0
        request.session['activities'] =[]
    print(request.session['gold'])

    context={
        "activities": request.session['activities'] 
    }

   
    return render(request, 'index.html',context)



def process(request):

    if request.method =="POST":
        location = request.POST['location']
        activities= request.session['activities']
        myGold = request.session['gold']
        if  location == 'farm':
            # earn 10 to 20 gold
            goldThisTerm= round(random.random()*10 +10)

        elif location == 'cave':
            goldThisTerm= round(random.random()*5 +10)

        elif location == 'house':
            goldThisTerm= round(random.random()*3 +2)
        else:
            winOrLose = round(random.random())
            if winOrLose==1:
                goldThisTerm= round(random.random()*1 +50)
            else:
                goldThisTerm= round(random.random()*0 +50)*-1



        
        # add gold this term to my_gold
        myGold += goldThisTerm
        request.session['gold'] = myGold
        
        
        #Date
        date_format = '%m/%d/%Y %H:%M:%S %Z'
        date = datetime.now(tz=pytz.utc)
        # print('Current date & time is:', date.strftime(date_format))
        date = date.astimezone(timezone('US/Pacific'))
        # print('Local date & time is  :', date.strftime(date_format))


        if goldThisTerm>0:
            stringToPopulate = f" Earned {goldThisTerm} from the {location} {date}"
        else:
            stringToPopulate = f" Lost {goldThisTerm} from the {location} {date}"



        activities.append(stringToPopulate)






    return redirect("/")
# Create your views here.

