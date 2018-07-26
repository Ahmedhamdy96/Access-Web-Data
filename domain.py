import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'


y = re.findall( '^From .*@([^ ]*)'   ,lin)
# ^From = Starting at the beginning of the line 
# .*@   = after one space and any number of characters followed by @ 
# get all non-blank characters 


print(y) # uct.ac.za

