import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@([^ ]*)',lin)
# @    = Look Through the string until you find @
# [^ ] = Non Blank Character  ^ = Not
# *    = match many of them 

print(y) # uct.ac.za

