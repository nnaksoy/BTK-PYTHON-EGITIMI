#1,100 e kadar
x=1
while x<=100:
    if(x%2==0):
        print(x)
    x+=1

name=''#boşluk a eşit olması false anlamındadır
while not name:
    name=input('isminizi giriniz: ')

print(f'merhaba, {name}')    

numbers=[]
i=0
while i<5:
    sayi=int(input('sayı: ' ))
    numbers.append(sayi)
    i+=1

numbers.sort()
print(numbers)