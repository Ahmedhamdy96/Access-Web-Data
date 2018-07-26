# Non-Greedy Matching in case of using * and + 

# ^F  = Starting with F 
# .+  = one or more character 
# ?:   = Ending with : but don't be greedy  

import re
x = 'From: Using the : character'
y = re.findall('^F.+?:',x)
print(y) # ['From:']  Not ['From: Using the :']     



