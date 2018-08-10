
import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET

url = input("Enter location : ")
url_h = urllib.request.urlopen(url)
data = url_h.read()
print("Retrieving" , url )
print("Retrieved " , len(data) , "characters" )

tree = ET.fromstring(data)
counts = tree.findall('comments/comment')

summ = 0

for item in counts :
    x = int(item.find('count').text)
    summ +=x

print("Sum Is :  " , summ)
