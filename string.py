'''
DATE:01TH DEC 2022
DAY: THURSDAY
TOPIC: STRINGS
AUTHOR: RAMA BHARGAVI
'''
print(dir(str))
a="rama"
print(type(a))#str
print(a.capitalize())#Rama
print(a.center(20))#     rama
print(a.center(20,'@'))#@@@@rama@@@@
print(a.casefold())#rama
a="rama"
k=a.encode()
print(k)#b'rama'
print(k.decode())#rama
print(a.upper())#RAMA
print(a.lower())#rama
print(a.isupper())#False
print(a.islower())#True
