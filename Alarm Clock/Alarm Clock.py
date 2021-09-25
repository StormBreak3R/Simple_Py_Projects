from datetime import datetime
from playsound import playsound

alarm_time = input("HH:MM:SS\n")
alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Your Alarm is set!")

while True:
    current_time = datetime.now()
    current_hour = current_time.strftime("%I")
    current_min = current_time.strftime("%M")
    current_sec = current_time.strftime("%S")
    current_period = current_time.strftime("%p")
    if current_period == alarm_period and current_hour == alarm_hour:
        if current_min == alarm_min and current_sec == alarm_sec:
            print("Its time. . .")
            playsound('sample.mp3')
            break
