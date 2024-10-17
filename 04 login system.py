attempts=3
while attempts !=0 :
    fname = input("Please input username: ")
    sname = input("Please input password: ")
    attempts -= 1
    if fname == "skibmaster" and sname == "mntyisgoat" :
        print("Hi charlie nathan white")
        break

if attempts == 0:
    print("unauthorised user ")
    print("no access")