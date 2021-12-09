#inheritance(kalıtım):miras alma
#person=> name, lastname, age, eat(), run(), drink()
#student(person), teacher(person)
class Person():
    def __init__(self,fname,lname):
        self.firstName=fname
        self.lastName=lname
        print('person created')
    def who_am_i(self):
        print('I am a person')

class Student(Person):
    def __init__(self,fname,lname,number):#personın constaki parametreleri de yazıyoz buna
        self.number=number
        Person.__init__(self,fname,lname)#bunu koymazsak student ın cons ı person ınkini ezer ve çalışmaz.
        #super().__init__(fname,lname) bu şekilde de olur
        print('student created')
    def who_am_i(self):# aynı isimli method tanımladğımızda temel sınıftakini ezer->override
        print('I am a student')


p1=Person('ali','yılmaz')
s1=Student('çınar','turan',123)
print(f'name: {p1.firstName}')
s1.who_am_i()
print(f'no: {s1.number}')