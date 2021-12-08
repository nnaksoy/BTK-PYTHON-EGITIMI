name='Çınar'
surname='Turan'
age=36
print('My name is {} {}'.format(name, surname))# süslü paantez yerine formatın içindeki değişken yazılır.
print('My name is {0} {1}'.format(name, surname))
print('My name is {1} {0}'.format(name, surname))
print('My name is {s} {n}'.format(n=name, s=surname))
print('My name is {} {} and I am {} years old.'.format(name, surname,'36'))
print('My name is {} {} and I am {} years old.'.format(name, surname,age))
result=200/700
print('the result is {r:1.4}'.format(r=result))#1 tam kısım ve virgülden sonra 4 basamak yaz
print(f'My name is {name} {surname} and I am {age} years old.')#yeni gelen bir özelik ve kolaylık