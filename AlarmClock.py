import datetime
import time
def alarm(alarm):
    while True:
        time.sleep(1)
        currentTime = datetime.datetime.now()
        now = currentTime.strftime("%H:%M:%S")
        print("Current Time is : ", now)
        print("Set alarm is At :", alarm)
        if now == alarm:
            print("Wake Up")
            break
setTime = input("Set Alarm Time in HH:MM:SS : ")
alarm(setTime)