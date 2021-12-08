name='Sadık'#karakter dizisi demesinin nedeni birden çok karakter olması. bu string ifadeniin her karakteri string dizisinin bir elemanıdır.
surname='Turan'
age=36
# print('My name is '+name+' '+surname+'and \nI am '+str(age)+' years old')

greeting='My name is '+name+' '+surname+'and \nI am '+str(age)+' years old'
print(len(greeting))#greeting ifadesninn kaç karakterli olduğunu söyler)
print(greeting[3])
print(greeting[len(greeting)-1])
print(greeting[-1])
print(greeting[2:6])# 2. indeksten 6 ya kadar yazar
print(greeting[3:])# 3 ten sonra kadar
print(greeting[:15])# baştan başlar 15 e kadar
print(greeting[2:40:2])# 2 den 40 a kadar 2 şer atlayarak alır