s = input() # take first string as input
t = input() # take second string as input
     
output = "Yes" # default output
     
def is_vowel(char):
  vowels = "aeiou" # vowels list for comparison
  found = char in vowels # check if char is in vowels list
  return found  # return the result
     
if len(s) != len(t): # check if the length of both strings are not equal
       output = "No" # if not equal then output is No
else:
  for i in range(len(s)):

    # check if the transformation is possible      
    if is_vowel(s[i]) and is_vowel(t[i]) or (not is_vowel(s[i])) and (not is_vowel(t[i])) :
      output = "Yes"
    else:
      output = "No"
      break  # break the loop if transformation is not possible
     
print(output) 