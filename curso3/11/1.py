import re

# hand = open('/home/carlo/Escritorio/words.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('^X-\S+:',line) :
#         print(line)

# Found numbers
x = 'My 2 favorite numbers are 48 and 10'
y = re.findall('[0-9]+',x) # '2', '48', '10'
print(y)

# Not found
y = re.findall('[AEIOU]+',x)
print(y)

m = 'From: Using the : character'
n = re.findall('^F.+:', m) # 'From: Using the :'
o = re.findall('^F.*:', m) # 'From: Using the :'
p = re.findall('^F.?:', m) # 'From:'
print(n)
print(o)
print(p)

# EMAILS
a = 'From stephen.marquard@uct.ac.za Sat Jun 5 09:14:16 2008'
b = re.findall('\S+@\S+',a)
print(b)

b = re.findall('^From (\S+@\S+)',a)
print(b)

b = re.findall('@([^ ]*)',a)
print(b)

b = re.findall('^From .*@([^ ]*)',a)
print(b)

b = re.findall('@(\S+)',a)
print("hola",b)

# other
hand = open('/home/carlo/Escritorio/words.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:',max(numlist))

# DOLLARS
a = 'We just received $10.00 for cookies'
b = re.findall('\$',a)
print(b)

a = 'From stephen.marquard@uct.ac.za Sat Jun 5 09:14:16 2008'
b = re.findall('@(\S+)',a)
print(b)

# Exercise 1: Sum all integers
hand = open('words.txt')
numlist = list()
suma = 0
for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+',line)
    if len(stuff) == 0 : continue
    for valor in stuff:
        num = int(valor)
        numlist.append(num)
        suma = suma + num
print(len(numlist))
print(numlist)
print(suma)
