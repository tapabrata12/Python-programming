# Python program for giving greetings the user according to the time (Homework)

import time

print(time.strftime("%H:%M:%S"))

if "04:00:00" <= time.strftime('%H:%M:%S') <= "08:00:00":
    print("Good Morning sir")

elif "08:00:01" <= time.strftime('%H:%M:%S') <= "11:59:59":
    print("Good Day sir")

elif "12:00:00" <= time.strftime('%H:%M:%S') <= "15:59:59":
    print("Good Noon sir")

elif "16:00:00" <= time.strftime('%H:%M:%S') <= "17:59:59":
    print("Good Afternoon sir")

elif "18:00:00" <= time.strftime('%H:%M:%S') <= "18:59:59":
    print("Good Evening sir")

else:
    print("Good Night sir")
