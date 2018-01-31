import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

#http://py4e-data.dr-chuck.net/comments_42.xml
# http://py4e-data.dr-chuck.net/comments_51143.xml

address = input('Enter location: ')
print('Retrieving', address)
uh = urllib.request.urlopen(address)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

suma = 0
contador = 0

results = tree.findall('.//count')
for item in results:
    suma = suma + int(item.text)
    contador = contador + 1

print('Count:',contador)
print('Sum:',suma)
