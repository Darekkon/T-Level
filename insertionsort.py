
def insertionsort(array):
    for i in range(1, len(array)):
        currentval = array[i]
        currentpos = i
        print(f"the current value is {currentval}, the current position is {currentpos}")

        while currentpos > 0 and array[currentpos-1] > currentval:
            array[currentpos] = array[currentpos-1]
            currentpos = currentpos -1
        array[currentpos]= currentval
    return array


# unsorted values
userarray = [13,464,367,7,4,6,6,787,2,43,46,865,1,3,]

# returned array will go to sorted array
sortedarray = insertionsort(userarray)

print(sortedarray)