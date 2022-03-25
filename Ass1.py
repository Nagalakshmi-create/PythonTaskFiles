# "This#string%contains^special*characters&.";   
# I want string without all special characters from above string

import re

sentence = "This#string%contains^special*characters&."
result = ""

for alphabet in sentence :
    if alphabet.isalpha():
        result += alphabet
    else:
        result = result
        
print(result)


output = re.sub("[#%^*&.]", " ", sentence)
print(output)