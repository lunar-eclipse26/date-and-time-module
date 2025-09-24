import random
import time
def GetRandomDate(startDate, endDate):
    print("printing random date between", startDate, "and", endDate)
    rng = random.random()
    dateFormat = '%m/%d/%Y'
    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))
    randomTime = startTime + rng * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate
print("random date = ", GetRandomDate("1/1/2019", "12/12/2024"))