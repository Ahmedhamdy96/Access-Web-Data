import json 
data = '''
[
	{"id":"001" , "x":"2" , "name":"ahmed "} , 
	{"id":"009" , "x":"7" , "name":"mohamed "}

]
'''

info = json.loads(data)
print('user count : ' , len(info))
for item in info : 
	print('Name : ' , item['name'])
	print('Id : ' , item['id'])
	print('Attribute : ' , item['x'])


