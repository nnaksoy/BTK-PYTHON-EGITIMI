#liste tipi
#bir bilgiye ulaşmak için key bilgisi gerekiyor. anahtar bilgisi.
#key-value 41=>kocaeli 34=>istanbul  
#plakalar={'key' : 'value' }
plakalar={'kocaeli':41 , 'istanbul': 34}
print(plakalar['kocaeli'])

plakalar['ankara']=6##olmayan bir key value ekleme
print(plakalar)
plakalar['kocaeli'] = 'new value' #var olan bir keye yen değer atama
print(plakalar['kocaeli'])

users={
    'sadikturan':{
        'age':36,
        'roles':['user'],
        'email':'sadik@gmail.com','address':'kocaeli',
        'phone':'1231321'},
         
         'cinarturan':{
        'age':2,
        'roles':['admin','user'],
        'email':'cinar@gmail.com','address':'kocaeli',
        'phone':'1231321'}
}
print(users['cinarturan']['age'])
print(users['cinarturan']['roles'][0])

ogrenciler={}
number=input("öğrenci no: ")
name=input("öğrenci adı: ")
surname=input("öğrenci soyadı: ")
phone=input("öğrenci telefon: ")

# ogrenciler[number]={
#     'ad':name,
#     'soyad':surname,
#     'telefon':phone
# }
# print(ogrenciler)

ogrenciler.update({
   number:{ 'ad':name,
    'soyad':surname,
    'telefon':phone}

})#bu iki şekilde de ekleme yapabiliriz.ama update le birden çok bilgi ekleyebiliriz
print(ogrenciler)
ogrno=input("öğrenci no: ")
ogrenci=ogrenciler[ogrno]
print(ogrenci)