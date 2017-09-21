import requests
import xml.etree.ElementTree as ET

url = requests.get('http://www.eurometeo.ru/ukraina/kiyvska-oblast/kiyiv/export/xml/data/')

file = open('/home/vlad/Documents/WeatherOfKiev.xml', 'w')
for index in url.text:
    file.write(index)
file.close()

tree = ET.parse('/home/vlad/Documents/WeatherOfKiev.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)




#print (url.content)