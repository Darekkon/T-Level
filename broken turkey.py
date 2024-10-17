

def turkeyDetails():
    weight = int(input("Enter in the weight of your turkey in pounds (lbs): "))
    turkType = input("Type in whether the turkey is stuffed [S] or unstuffed [U]: ")
    return weight, turkType 

def calcUnstuffed(weight):
    if(weight >= 4 and weight < 6):
        return "1.5-2.25"
    elif(weight >= 6 and weight < 8):
        return "2.25-3.25"
    elif(weight >= 8 and weight < 12):
        return "2.75-3"
    elif(weight >= 12 and weight < 14):
        return "3-3.75"
    elif(weight >= 14 and weight < 18):
        return "3.75-4.25"
    elif(weight >= 18 and weight < 20):
        return "4.25-4.50"
    elif(weight >= 20 and weight < 24):
        return "4.5-5"
    else:
        return "10"
    return 0

def calcStuffed(weight):
    if(weight >= 6 and weight < 12):
        return "3-3.5"
    elif(weight >= 12 and weight < 14):
        return "3.5-4"
    elif(weight >= 14 and weight < 18):
        return "4-4.25"
    elif(weight >= 18 and weight < 20):
     return "4.25-5.25"
    elif(weight >= 20 and weight < 24):
        return "4.75-5.25"
    else:
        return 0
    while(weight <2):
        print("Your turkey is over 2 pounds in weight")
    return 0

def deepFry():
    return input("Would you like to deep fry your turkey [Y/N]: ")
    

def deepFryTurkey(weight):
    calc = 5 + (3**weight)
    return calc

print("Welcome to the Turkey cooking program, follow the steps to find out how to cook your turkey!!")

iTurkeyWeight, iTurkeyType = turkeyDetails()

if(iTurkeyType.upper() == "U"):
    iOriginalCookTime = calcUnstuffed(iTurkeyWeight)
    print("The cooking time for the turkey is", iOriginalCookTime, "hours at 325 degrees farenheight")
elif(iTurkeyType.upper() == "S"):
    iOriginalCookTime = calcStuffed(iTurkeyWeight)
    print("The cooking time for the turkey is", iTurkeyWeight, "hours at 325 degrees farenheight")

sDeepFriedChoice = deepFry()

if(sDeepFriedChoice == "Y"):
    print("After cooking, you will need to add the following to heat oil to 350 degrees and cook for", calcStuffed(iTurkeyWeight), "minutes")
else:
    print("The turkey is done!!")