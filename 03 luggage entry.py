weight = input("How much kg does your luggage weigh? ")

def round_to_next5(n):
    return n + (5 - n) % 5

if int(weight) <= 100 :
    print("your luggage weighs " + weight + "kg and is in the 100kg weight limit")
elif int(weight) > 100 :
    overw = int(weight) - 100 
    print("your luggage weighs " + weight + "kg and is over the 100kg weight limit")
    print("your luggage is " + str(overw) +"kg over weight")
    rounded = round_to_next5(overw)
    price = rounded / 5
    print("you will have to pay £" + str(price) +" due to the excess weight")