#koşul belirtelim. sağlamadığı halde exception üretelim

# x=10
# if x>5:
#     raise Exception('x 5 ten büyük değer alamaz')

def check_password(psw):
    import re
    if len(psw)<8:
        raise Exception ('parola en az 7 karakter olmalıdır')
    elif not re.search('[a-z]',psw):#psw içinde a dan z ye kadar harf araması yapar yoksa bu bloğa girer
        raise Exception('parola küçük harf içermelidir')
    elif not re.search('[A-Z]',psw):
        raise Exception('parola BÜYÜK harf içermelidir')   
    elif not re.search('[0-9]',psw):
        raise Exception('parola RAKAM  içermelidir') 
    else:
        print('geçerli parola')
        
password='12345678aA'
try:
   check_password(password)
except Exception as ex:
    print(ex)
else:
    print('geçerli parola: else')