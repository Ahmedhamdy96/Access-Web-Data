
import xml.etree.ElementTree as ET
input = '''
<stuff>
    <users>
        <user x="2">
            <name>Ahmed</name>
            <id>001</id>
        </user>
        <user x="7">
            <name>Mohamed</name>
            <id>009</id>
        </user>
    </users>
</stuff>
'''
stuff = ET.fromstring(input) # class
lst = stuff.findall('users/user')
print("User count : " , len(lst)) # 2

for item in lst :
    print('Name : ' , item.find('name').text)
    print('Id : ' , item.find('id').text)
    print('Attribute : ' , item.get("x"))



# User count :  2
# Name :  Ahmed
# Id :  001
# Attribute :  2
# Name :  Mohamed
# Id :  009
# Attribute :  7
