#tip dönüştürme işlemleri
"""
x=input('1. sayı: ')
y=input('2. sayı: ')
#toplam=x+y-> inputtan gelenler string algılanır. bunun sonucu 1020 olur. toplamasını istiyorsk stringi int e çevirmeliyiz

print(type(x))
print(type(y))
toplam=int(x)+int(y)

print(toplam)"""


x=5
y=2.5
name="Çınar"
isOnline=True

# print(type(x))
# print(type(y))
# print(type(name))
# print(type(isOnline))

#type conversion:

#int to float
"""
x=float(x)
print(x)
print(type(x))"""
#float to int
'''
y=int(y)
print(y)
print(type(y))'''

#int to string
"""result=str(x)+str(y)
print(result)
print(type(result))"""

#bool to string
"""isOnline=str(isOnline)
print(isOnline)
print(type(isOnline))"""

isOnline=int(isOnline)
print(isOnline)
print(type(isOnline))#true=1 false=0

"""
yarı çapı alınan dairenin çevresini ve alanını hesaplama
"""
r=float(input('yarı çap: '))
pi=3.14
alan=pi*r**2
cevre=2*pi*r
print('alan: '+str(alan)+' cevre: '+str(cevre))