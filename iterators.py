#13-pythonda yenileyiciler
liste=[1,2,3,4,5]
#liste bir iterable obje.
#list bir clas. iterable olması için iter metodunu içermesi gerekyor.iteratör ü iterable objeden oluşturabilirz. ve next iteroterle elemanlara ulaşabilyoruz. for döngüsü biizm için aslında bir iteratör oluşturuyor
iterator=iter(liste)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

#list gibi bir clası kendimiz oluşturmak istersek ister metdou kulanmamız gerekir onan bu yapıyı bilmeliyiz.