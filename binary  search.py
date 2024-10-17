
def binsearch(tofind, items) :
    firstindex = 0
    lastindex = len(items) - 1
    while(firstindex<=lastindex):
      midindex = (firstindex + lastindex) // 2
      print(f"this is the middle index: {midindex} ")
      if items[midindex] == tofind:
         print("the num is in the list so skib")
         return 0
      elif items[midindex]<tofind:
         firstindex = midindex + 1
      else:
         lastindex = midindex - 1

num = int(input("input the number you would like to find ?\n"))
sortarray = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

binsearch(num, sortarray)