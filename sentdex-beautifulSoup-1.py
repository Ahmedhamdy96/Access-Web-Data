import bs4 
import urllib.request 

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs4.BeautifulSoup(sauce,'lxml')  # this line organise the code and write it in a good way to make it easy for reading for us  

#print(soup)      			# prints the source code of the page 

print(soup.title)                       # prints the title element of the page  <title> Python Programming Tutorials </title>

print(soup.title.string)		# 						Python Programming Tutorials 
print(soup.title.text)			#						Python Programming Tutorials  			


print(soup.p) 				# prints the paragraph element of the page  <p> bla bla bla ...</p>


print("-------------------------" )
#print(soup.find_all('p'))		# to get a list containing all <p> tags of the page  


#for paragraph in soup.find_all('p'):
	#print(paragraph , "\n" )
	#print(paragraph.text) 		# to get the text between <p> .... </p>





for url in soup.find_all('a'):		# to get all <a> ...  </a> tags  
	#print(url)
	#print(url.text)		# to get the text between <a>...</a> tags  
	print(url.get('href'))		# to get the actual links 








	
