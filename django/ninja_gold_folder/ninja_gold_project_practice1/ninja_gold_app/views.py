from django.shortcuts import render,redirect, HttpResponse
import random , pytz
from datetime import datetime
from pytz import timezone 


def create_date():
    #Date
    date_format = '%m/%d/%Y %H:%M:%S %Z'
    date = datetime.now(tz=pytz.utc)
    # print('Current date & time is:', date.strftime(date_format))
    date = date.astimezone(timezone('US/Pacific'))
    # print('Local date & time is  :', date.strftime(date_format))
    return date

def random_reward(lower_bound, upper_bound):
    randomReward= round(random.random()*lower_bound + upper_bound)
    return randomReward




def index(request):
    if "gold" not in request.session or "result" not in request.session:
        request.session['gold']=0
        request.session['result'] = []
        request.session['textColor'] = 'green'

    
    
    
    return render(request, 'index.html')

def reset(request):
    request.session['gold'] =0
    request.session['result'] =[]
    return redirect('/')


def process(request):


    globalGold = request.session['gold']
    earned = True
    sentenceColor = 'green'
    now_formatted = create_date()

    if request.method =="GET":
        redirect('/')

    clickedEvent = request.POST['event']

    print(clickedEvent)
    print(random_reward(10,20))

    if clickedEvent=="casino":
        print("casinocasinocasinocasinocasino")

        #random 0 or 1 to determine + or -
        earnLose = random.randint(0, 1)
        if earnLose == 0:
            eventGeneratedGold = random_reward(0,50)
        else :
            eventGeneratedGold = -1*random_reward(0,50)
            earned = False
            sentenceColor = 'red'
    
    elif clickedEvent == "farm":
            eventGeneratedGold = random_reward(10,20)
    elif clickedEvent=="cave":
            eventGeneratedGold = random_reward(5,10)
    elif clickedEvent=="house":
            eventGeneratedGold = random_reward(2,5)

    if earned == False:
        message = f"Lost {eventGeneratedGold} from the {clickedEvent}! {now_formatted}"
    else:
        message = f"Earned {eventGeneratedGold} from the {clickedEvent}! {now_formatted}"
        
    



    

    request.session['gold'] += eventGeneratedGold
    request.session['result'].append(message)
    request.session['textColor'] = sentenceColor

    print("request.session['textColor']request.session['textColor']" , request.session['textColor'])




    return redirect('/')


  