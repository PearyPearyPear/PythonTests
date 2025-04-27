import time
import os

s = int(input("Enter your timer [sec]: "))
t = s
for i in range(0, s):
    t -= 1
    print(f"{t} seconds left")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
print("Timer ended")