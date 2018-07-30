import bs4 
import urllib.request 	


sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs4.BeautifulSoup( sauce , 'lxml') 

nav = soup.nav 

for url in nav.find_all('a'): 
	print(url.get('href'))


print('=============================')

#body = soup.body 

#for paragraph in body.find_all('p'):
#	print(paragraph.text)



for div in soup.find_all('div',class_='body'):   # to get the text between  <div class = "body" > </div>
	print(div.text)









