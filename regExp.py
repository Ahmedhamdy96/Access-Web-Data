# Regular Expressions using Python 3.5.2 
# [0-9] any digit 0,1,2,....,9 
# + one or more digits 
# re.findall() give us a list of the matches 

import re 
x = 'My 2 favorite numbers are 19 and 42' 
y = re.findall('[AEIOU]+',x) 
print(y) # []





