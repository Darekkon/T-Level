import random      
score = 0
pa = input("do you want to play ?")
randnum = random.randint(1,10) 
while pa != "no" :            
    while True :
        guess = input ("guess a number from 1 to 10\n")
        if int(guess) > randnum :
            print("the number is lower")
        elif int(guess) < randnum :
            print("the number is higher")
        elif int(guess) == randnum :
            print("well done you win")
            score += 1
            randnum = random.randint(1,10) 
            pa = input("do you want to play again?")
            if pa == "no" :
                break
print("your final score is " + str(score))
