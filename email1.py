# \S+   At Least One Non-Whitespace character

# Parentheses ()  are not part of the match , but they tell WHERE TO START and STOP what string to extract 

import re
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('^From (\S+@\S+)',x)
print(y) # ['stephen.marquard@uct.ac.za']


