#class
class Person:
    #attributes
    #class attributes ve object attributes lar vardır
    #object attributeları constructorm içinde tanımlıcaz
    adress='no information'

    #constructor(yapıcı metod)
    def __init__(self,name,year):

        #object attributes
        self.name=name
        self.birthyear=year

    #instance methods
    def intro(self):
        print('hello there '+self.name)

    def calculateAge(self):
        return 2019-self.birthyear
    pass

p1=Person('ali',1990) #p1 objesini tanımladık. person clasının örneği
p2=Person(name='yağmur',year=2001)

#updating
p1.adress='kocaeli'

print(f'name: {p1.name} year:{p1.birthyear} adress:{p1.adress} yaşım:{p1.calculateAge()}' )
p1.intro()
