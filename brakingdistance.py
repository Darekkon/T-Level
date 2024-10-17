import os
import time

def brakingdistance():
    speed = 0
    while int(speed) > 50 or int(speed) < 10 :
        speed = input("what is the speed ")
    brakedist = int(speed) / 5
    ground = input("is ground wet ").lower()
    if ground == "yes":
        brakedist = (brakedist * 1.5)
    print(brakedist)

while True:
    brakingdistance()
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')