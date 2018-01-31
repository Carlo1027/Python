import urllib.request, urllib.parse, urllib.error

# Using urllib in Python
# fhand = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
# for line in fhand:
#     print(line.decode().strip())



# Like a File
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
#
# counts = dict()
#
# for line in fhand:
#     words = line.decode().split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)



# Reading Web Pages
fhand = urllib.request.urlopen('http://dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())
