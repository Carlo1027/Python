import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# http://py4e-data.dr-chuck.net/comments_51141.html
# sumar todos los números de la tabla

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

numlist = list()
count = 0
suma = 0
tags = soup('span')
for tag in tags:
    count += 1
    num = int(tag.contents[0])
    numlist.append(num)
    suma = suma + num
print('Count',count)
print('Sum',suma)
