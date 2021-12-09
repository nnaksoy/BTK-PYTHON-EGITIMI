#def square(num): return  num**2
square=lambda num:num**2
result=square(2)
print(result)
numbers=[1,3,5,9]
result=list(map(lambda num:num**2,numbers))#ismi olmayan bir fonksiyon.bir kere çalıştırılacak bir işlemi fonksiyon yerine lambda olarak yapabilirz.
#listedeki her bir elemana ulaşık her birini fonksiyondan geçiren metoddur.maptan dönen sonucu list e atıyo.
print(result)