# \S+   At Least One Non-Whitespace character

import re
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('\S+@\S+',x)
print(y) # ['stephen.marquard@uct.ac.za']


