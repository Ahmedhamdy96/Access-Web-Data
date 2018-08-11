# json represents datat as nested lists and dictionaries

import json 
data = '''
{ 
		"name":"ahmed" , 
		"phone":{ "type" : "int1" , "number" : "+123456" }, 
		"email":{ "hide" : "yes" }
		
} 
'''

info = json.loads(data)
print('Name: ' ,info["name"]) 
print('Hide: ' ,info["email"]["hide"])

