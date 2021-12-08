my_list=[1,2,3]
my_list=['bir',2,True,5.6]
print(my_list)
list1=['one','two','three']
list2=['four','five','six']
numbers=list1+list2#2 dizi toplanır numbers a 2sinin elemanları aktarılır
print(numbers)
print((len(numbers)))

user1=['Sadık',36]
user2=['Çınar',2]
users=[user1,user2]
print(users[1][0])#iç içe listelerde 1. indekstekinin 0. indeksini verir.
print('Çınar'in user2)#çınar user2 nin elemanı mıdır
print(user2+['Turan','mühendis'])#listeye ekleme yapma
del user2[1]#silme işlemi
print(user2)