
attempts=3
while attempts !=0 :
    fname = input("what is your first name ? ")
    sname = input("what is your surname ? ")
    attempts -= 1
    if fname == "darek" and sname == "konstanty" :
        print("Hi darek")
        break

if attempts == 0:
    print("unauthorised user ")
    print("no access")

 