import random
import time
def get_random_date(startDate,endDate):
    randomGenerator=random.random()
    format='%m/%d/%Y'
    startTime=time.mktime(time.strptime(startDate,format))
    endTime=time.mktime(time.strptime(endDate,format))
    randomTime=startTime+randomGenerator*(endTime-startTime)
    randomDate=time.strftime(format,time.localtime(randomTime))
    return randomDate
print(get_random_date("10/7/2026","12/26/2026"))