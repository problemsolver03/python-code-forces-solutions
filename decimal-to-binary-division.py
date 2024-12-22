# decimal to binary using division method

decimal = int(input()) # taking and conveting to int
binary =[] # array to store the binary values for output

while decimal > 0: # exit condition to exit the loop
    if decimal % 2 == 0: # if no remainder after divison by 2 adding 0 to binary list
        binary.append(0)
        decimal = (decimal // 2) # floor divison to update the new value to decimal
    else:
        binary.append(1)
        decimal = (decimal // 2) # floor divison to update the new value to decimal    

print("".join(map(str,binary[::-1]))) # converting to string to print output
