
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")


summ = []
tags = soup('span')
for tag in tags:
    summ.append(tag.contents[0])
    
result = 0 
count = 0 
for i in summ:
    result = result + int(i) 
    count +=1 

print('count ', count)
print('sum ' , result)

