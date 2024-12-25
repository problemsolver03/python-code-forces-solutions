# decimal to binary using substraction method

decimal = int(input()) # taking and conveting to int
powers_list =[] # array for storing the power values
binary =[] # array to store the binary values for output
current_decimal = 0 # variable for updating the decimal post substraction

for i in range(decimal):
    power_value  = (2**i) # powered value
    if  power_value <= decimal: # checking if the powered value is less than input to continue loop
     powers_list.append(power_value) 
    else:
     break 
powers_list = powers_list[::-1] # reversing powered values

for i in range(len(powers_list)):
   if(i==0): 
    current_decimal = decimal - powers_list[i]
    binary.append(1) # appending 1 by default to binary list if the index is 0
   else:    
      if (current_decimal - powers_list[i]) >= 0 : # checking if the substraction difference is greater to 0 
       current_decimal = current_decimal - powers_list[i]
       binary.append(1)
      else:
       binary.append(0) 
            
print_binary  = ''.join(map(str, binary)) # converting to string to print output
print(print_binary)
# if len(print_binary) > 3:
#   print(print_binary)
# else:
#   missing_zeros_length = 4-len(print_binary)
#   missing_zeros = "0"*missing_zeros_length
#   print(missing_zeros+print_binary)
 