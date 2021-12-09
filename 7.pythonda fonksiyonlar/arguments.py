def changeName(n):
     n='ada'#value type
    
name='yiğit'
changeName(name)
print(name)

def change(n):
    n[0]='istanbul'#referance type n ye adres kopyalama oluyor


sehirler=['ankara','izmir']
change(sehirler[:])#sciling. parçalama yöntemi ile kopyalama yapıyo.sadece kopyanın 0. indeksini değiştirir.
print(sehirler)
change(sehirler)
print(sehirler)

def add( *params):# parametre sayısı sınırsızdır.tuple listesidir
    return sum(params)#bu method toplama yapar

print(add(10,20,30,40,50))

def displayUser(**args):#dictionary.farklı sayıda farklı parametre türleri
    for key,value in args.items():
        print(f'{key} is {value}')


displayUser(name='Çınar',age=2,city='istanbul')
displayUser(name='ada',age=12,city='kocaeli',phone='1234')
displayUser(name='yiğit',age=14,city='ankara',phone='12345',mail='yigit@gmail.com')

def muyFunc(a,b, *args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

muyFunc(10,20,30,40,50,key1='value1',key2='value2')