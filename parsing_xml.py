
import xml.etree.ElementTree as ET # to parse xml
data = '''<person>
<name>Ahmed</name>
<phone type="int1"> +123456</phone>
<email hide="yes"/>
</person> '''

tree = ET.fromstring(data)
print('Name:' , tree.find('name').text)
print('Attr:' , tree.find('email').get('hide'))

# Name:Ahmed
# Attr:yes
