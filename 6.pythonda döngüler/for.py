numbers=[1,2,3,4,5]
for num in numbers:#listenşn içerisininden tek tek elemanları al ve num değişkenin içine at yazdır
    print(num)

name='sadık turan'
for n in name:
    print(n)

tuple=[(1,2),(3,4),(3,2),(4,1)]
for a,b in tuple:
    print(a, b)

d={'k1':1, 'k2':2, 'k3':3}
for item in d :#sadece keyleri verir
    print(item)

for item in d.items():
    print(item)

for key,value in d.items():
    print(value)