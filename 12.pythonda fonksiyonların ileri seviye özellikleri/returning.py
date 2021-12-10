#fonkssiyondan bi fonksiyon döndürme



def usalma(number):
    def inner(power):
        return number**power
    return inner

two=usalma(2)#two burda us alma 2 fonksiyonuna eşitleniyo
print(two(3))#burdada retrun edilen fonksiyona tekrar değer gönderiyoruz

def yetki_sorgula(page):
    def inner(role):
        if role=='Admin':
            return print(f"{role} rolü {page} sayfasına ulaşabilir.")
        else:
            return print(f"{role} rolü {page} sayfasına ulaşamaz.")
    return inner

user1=yetki_sorgula("Product edit")
print(user1("Admin"))
print(user1("User"))

def islem(islem_adi):
    def toplam(*args):
        toplam=0
        for i in args:
            toplam+=i
        return toplam
    
    def carpma(*args):
        carpim=1
        for i in args:
            carpim*=i
        return carpim

    if islem_adi=="toplama":
        return toplam
    else:
        return carpma

toplama=islem("toplama")
print(toplama(1,3,5,7,8))

carpma=islem("carpma")
print(carpma(4,5,2))