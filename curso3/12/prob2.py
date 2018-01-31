import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# http://py4e-data.dr-chuck.net/known_by_Rhoridh.html

url = input('Enter ')

count = input('Enter count: ')
count = int(count)

position = input('Enter position: ')
position = int(position)

print(url)
for i in list(range(0,count)):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    numlist = list()
    tags = soup('a')

    for tag in tags:
        numlist.append(tag.get('href', None))
    url = numlist[position-1]
    print(url)
