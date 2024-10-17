valtosort = [12,77,34,567,123,23,5,78,19]

indexlen = len(valtosort) -1

bsorted = False
while not bsorted:
    bsorted = True
    for i in range(0,indexlen):
        if valtosort[i] > valtosort[i+1]:
            bsorted = False
            switch = valtosort[i]
            valtosort[i] = valtosort[i+1]
            valtosort[i+1] = switch     
print(valtosort)
