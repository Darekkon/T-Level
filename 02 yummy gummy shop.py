import math


gummies = input("how many gummies do you want ? ")
price = int(gummies) * 0.5
rprice = math.ceil(price*100)/100  
print("Your price is £" + str(rprice)) 
VAT = int(gummies) * 0.1
rVAT = math.ceil(VAT*100)/100  
print("There is a 20% VAT which comes out to £" + str(rVAT) ) 
VATprice = int(gummies) * 0.6
rVATprice = math.ceil(VATprice*100)/100  
print("Incuding Vat your final price is £" + str(rVATprice)) 