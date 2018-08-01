import urllib.request 
import urllib.parse 
import urllib.error

import ssl 

import re
import bs4 

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL : ')
count = int(input('Enter Count : '))
position = int(input('Enter Position : '))

for i in range(0,count+1):
	html = urllib.request.urlopen(url).read()
	soup = bs4.BeautifulSoup(html,'html.parser')
	print('Retrieving : ' , url)
	tags = soup('a')
	pos = 0 
	for tag in tags :
                if pos == position-1 :
                        url = tag.get('href' , None)
                        break
                pos +=1 

