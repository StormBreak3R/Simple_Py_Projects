from datetime import datetime
from playsound import playsound

alarm_time = input("HH:MM:SS\n") #taking input 
alarm_hour = alarm_time[0:2]  # spliting string for specific time
alarm_min = alarm_time[3:5] 
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Your Alarm is set!")

while True:
    current_time = datetime.now()   #current time from datetime module
    current_hour = current_time.strftime("%I")   #format the time in different desirable ways (for details visit: strftime.org
    current_min = current_time.strftime("%M")
    current_sec = current_time.strftime("%S")
    current_period = current_time.strftime("%p")
    if current_period == alarm_period and current_hour == alarm_hour: #comparing both time
        if current_min == alarm_min and current_sec == alarm_sec:
            print("Its time. . .")
            playsound('sample.mp3')  #to play alarm
            break
