import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')

print('Retrieving ',url)

fhand = urllib.request.urlopen(url)
hola = fhand.read()
print('Retrieved',len(hola),'characters')
data = hola.decode()
info = json.loads(data)
print('Count',len(info['comments']))

suma = 0
for item in info['comments']:
    suma = int(item['count']) + suma
print('Sum:',suma)
