#class
class Person:
    #attributes
    #class attributes ve object attributes lar vardır
    #object attributeları constructorm içinde tanımlıcaz
    adress='no information'#mesela pi sayısı gibi ortak bir değer class seviyesinde tanımlanabilir

    #constructor(yapıcı metod)
    def __init__(self,name,year):#init metodu. self clastan üretilen objeleri temsil eder. obje üzerine değer aktarmak istersen self kullancaz. hangi özellikleri eklemek istiyosan selften sonra parametre olarak ekle
        #init metdou her çalıştırılan obje için otomatik çalışır.

        #object attributes
        self.name=name
        self.birthyear=year

    #methods
    pass# pass keywordü yer tutucudur. içi boş class olsa da hata almayız 
#object=instaance
#accesing object attributes
p1=Person('ali',1990) #p1 objesini tanımladık. person clasının örneği
p2=Person(name='yağmur',year=2001)

#updating
p1.adress='kocaeli'

print(f'name: {p1.name} year:{p1.birthyear} adress:{p1.adress}' )