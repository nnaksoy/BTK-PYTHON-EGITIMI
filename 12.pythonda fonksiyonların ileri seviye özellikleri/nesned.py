#fonksiyonlar bir objedir.
def greeting(name):
    print('hello ',name)

sayhello=greeting#sayhelloyu greating in adresine eşitliyoruz

print(sayhello)
print(greeting)

del sayhello#bunu silmiş olmak o adresi değil tanımlmasını silmektir.
print(greeting)

#ENCAPSULATİON:İÇTEKİ FONKSİYON KENDİNE YENİ BİR ÇALIŞMA ALANI TANIMLIYOR VE DIŞTAKİ ŞLEMLER ONU ETKİLEMİYOR. VE OUTER DIŞINDA ÇALIŞMAZ
def outer(num1):
    print('outer')
    def inner_increment(num1):
        print('inner')
        return num1+1
    num2=inner_increment(num1)#bu içteki fonksiyonu dıştakının içinde çağırmazsak bu fonksiyona girmez
    print(num1,num2)
outer(10)

def factorial(number):
    if not isinstance(number,int):
        raise TypeError("number must be int")
    def inner_factorial(number):
        if number <= 1:
            return 1
        return number*inner_factorial(number-1)
    return inner_factorial(number)

print(factorial(4))