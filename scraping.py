#import urllib2
#from bs4 import BeautifulSoup
#quote_page = 'http://www.bloomberg.com/quote/SPX:IND'
#page = urllib2.urlopen(quote_page)
#soup = BeautifulSoup(page, 'html.parser')
#name_box = soup.find('a', attrs={'class': 'bb-nav-categories__link'})
#name = name_box.text.strip()
#print(name)

import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.weifastpay.com/productos/")
#print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

name_box = soup.find_all('div', class_= 'description')
for line in name_box:
	name = line.text.strip()
	print(name)
