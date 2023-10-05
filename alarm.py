import time
import os 


a = int(input("Enter the time to stop the alarm ="))



for i in range (1,60):
    time.sleep(1)
    print(i,"sec")
    if i==a:
        os.system('start alarm.mp3')
        break
