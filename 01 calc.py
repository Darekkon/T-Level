import time

num1 = input("input your first number ")
num2 = input("input your second number ")
add = int(num1) + int(num2)
time.sleep(1)
print(str(num1)+" + "+str(num2)+" = "+str(add))
sub = int(num1) - int(num2)
time.sleep(1)
print(str(num1)+" - "+str(num2)+" = "+str(sub))
Mult = int(num1) * int(num2)
time.sleep(1)
print(str(num1)+" x "+str(num2)+" = "+str(Mult))
div = int(num1) / int(num2)
time.sleep(1)
print(str(num1)+" % "+str(num2)+" = "+str(div))