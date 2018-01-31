# def computepay(h,r):
#     if h <= 40 :
#         pay = h*r
#         return pay
#     else :
#         pay = (h-40)*r*1.5 + 40*r
#         return pay
#
# hrs = input("Enter Hours:")
# h = float(hrs)
# rph = input("Enter Rate:")
# r = float(rph)
#
# x=computepay(h,r)
# print(x)

# #Maximum and Minimum
# largest = None
# smallest = None
# while True:
#     num = input("Enter a number: ")
#     if num == "done" : break
#     try:
#         convert = int(num)
#     except:
#         print('Invalid Input')
#
#     if smallest is None:
#         smallest = convert
#     elif smallest > convert:
#         smallest = convert
#
#     if largest is None:
#         largest = convert
#     elif largest < convert:
#         largest = convert
#
# print("Maximum is", largest)
# print("Minimum is", smallest)

# #week 6
# text = "X-DSPAM-Confidence:    0.8475"
#
# lugar = text.find('0')
# numero = float(text[lugar:])
# print(numero)

# fhand = open('hola.txt')
# inp = fhand.read()
# print(len(inp))


# week 9
# fname = input("Enter file name: ")
# fh = open(fname)
# count = 0
# lst = list()
# for line in fh:
#     if not line.startswith("From ") : continue
#     count = count + 1
#     print(line.rstrip().split()[1])
#     lst.append(line.rstrip().split()[1])
# # print(lst)
# print("There were", count,"lines in the file with From as the first word")
#
# ccc = dict()
# for email in lst:
#     ccc[email] = ccc.get(email,0)+1
# # print(ccc)
#
# bigword = None
# bigcount = None
# for word,count in ccc.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count
# print(bigword, bigcount)



# fname = input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
#     x = line.rstrip()
#     y = x.split()
#     for m in y:
#         if m not in lst:
#             lst.append(m)
# lst.sort()
# print(lst)

# week 10
fname = input("Enter file name: ")
fh = open(fname)
count = 0
lst = list()
for line in fh:
    if not line.startswith("From ") : continue
    count = count + 1
    lst.append(line.rstrip().split()[5][:2])

ccc = dict()
for email in lst:
    ccc[email] = ccc.get(email,0)+1

bigword = None
bigcount = None
for word,count in sorted(ccc.items()):
    print(word, count)

# week 11
