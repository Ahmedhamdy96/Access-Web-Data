# Greedy Matching in case of using * and + 

# ^F  = Starting with F 
# .+  = one or more character 
# :   = Ending with : 

import re
x = 'From: Using the : character'
y = re.findall('^F.+:',x)
print(y) # ['From: Using the :']     Not ['From:']



