import urllib.request
import urllib.parse
import urllib.error
import json

url = input("Enter Location : ")
print("Retrieving  : " , url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()

js = json.loads(data)
print("Retrieved  : " , len(js) , " Characters ")

summ = 0
for item in js["comments"]:
    summ = summ+item["count"]

print("========================")
print(summ)
