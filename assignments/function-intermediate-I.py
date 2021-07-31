import random
def randInt(lowBound=0, highBound=100):
    if lowBound>highBound:
        print("wrong bounds")
    else:
        randNum = random.random()*(highBound-lowBound) +lowBound
        randNum = round(randNum)
        return randNum

result =randInt(40,30)
print(result)