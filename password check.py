inumberinpass = 0 


password = input("input your password ")

poorpass = ["password","123456","12345678","1234","qwerty","12345", "dragon","baseball","football","letmein","monkey","696969"]

bFound = False 
for i in range(len(poorpass)):
    if password == poorpass[i]:
        print("this password is to weak use a stronger one")
        bFound = True

if len(password) < 8:
    print("the password is too short, please use atleast characters ")
    bFound = True

for i in range(len(password)):
    if password[i].isdigit():
        inumberinpass += 1

if inumberinpass == 0:
    print("you should add a number")
    bFound = True

if bFound == False:
    print("your password is secure")