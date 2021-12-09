#döngülerde kullanabileceğimiz bazı metodlar:

#range
for item in range(2,20,2):#range metodu 2 den 20 e kadar 2 şer artan bir liste hazırlar
    print(item)

#enumerate
greeting='Hello There'
for item in enumerate(greeting):#index numaralarına karşılık gelen karakterleri gruplandırır. liste şeklinde oluşturur
    print(item)

#zip
list1=[1,2,3,4,5]
list2=['a','b','c','d','e']
print(list(zip(list1,list2)))#listeleri eşleştirerek birleştirir