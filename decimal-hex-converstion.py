# decimal = int(input())
decimal  = 256
hex_list =[0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]

output= ""



def isPower (x, y):
    pow = 1
    while (pow < y):
        pow = pow * x
    return (pow == y)

if decimal<1:
   output = str(decimal)+str(decimal)
elif decimal < 10 and decimal >1:
   output = "0"+str(decimal)
elif decimal < 16 and decimal >9:
   output = "0"+ str(hex_list[decimal])   
else:
   first_bit = decimal//16
   if first_bit < 256 :
    remainder = hex_list[decimal % 16]
    output = str(first_bit)+str(remainder)
   else:
    print("coming soon")   

print(isPower(16,16))