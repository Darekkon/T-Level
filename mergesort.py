
def mergesort(array):
    lengtharray = len(array)
    if(lengtharray>1):
        midlen = lengtharray //2
        larr = array[:midlen]
        rarr = array[midlen:]
        print(f"this is left array {larr}")
        print(f"this is right array {rarr}")
        mergesort(larr)
        mergesort(rarr)
        ilind = 0
        irind = 0
        imind = 0
        while ilind < len(larr) and irind < len(rarr):
            if larr[ilind] < rarr[irind]:
                array[imind] = larr[ilind]
                ilind += 1
            else:
                array[imind] = rarr[irind]
                irind +=1
            imind +=1
        print(array)
        while ilind < len(larr):
            array[imind] = larr[ilind]
            ilind +=1
            imind +=1
        while irind < len(rarr):
            array[imind] = rarr[irind]
            irind +=1
            imind +=1
    return array
        

userarray = [1,6,4,6,86,457,6,54,34,43324,65,7865,123,4567,22]
print(mergesort(userarray))