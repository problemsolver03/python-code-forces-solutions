binary = list(map(int, input()))
powers_list =[] # array for storing the power values
reverse_binary = binary[::-1]
sum = 0
for i in range(len(binary)):
    power_value  = (2**i) # powered value 
    if(reverse_binary[i]==1):
      sum += power_value # incrementing sum by power value   
print(sum)