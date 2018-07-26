# a code to read a file contains words and numbers 
# extract all numbers .. compute the sum of them  
import re 

h = open('sample.txt')
file = h.read()

numbers = []
newNumbers = [] 
result = 0 

for line in file :
	numbers = re.findall('[0-9]+',file)  # items is str

for i in numbers : 
	newNumbers.append(int(i)) # create a new list of integers 

for i in newNumbers : 
	result += i 
print(result)