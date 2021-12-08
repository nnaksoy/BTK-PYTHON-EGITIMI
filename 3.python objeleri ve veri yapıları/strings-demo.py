website='http://www.sadikturan.com'
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1)course karakter dizisinde kaç karakter bulunmaktadır?
print(len(course)," adet karakter vardır.")
 # 2) website içinden www karakterini al
print(website[7:10])
# 3) website içinden com karakterini al
print(website[len(website)-3:len(website)])
# 4) course içinden ilk 15 ve son 15 karakterleri al
print(course[:15])
print(course[len(course)-15:])
# = print(course[-15:])
 #course ifadesini tersten yazdır
print(course[::-1])

name,surname,age,job='Bora', 'Yılmaz', 32, 'mühendis'
# 6) yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis
print('Benim adım {} {}, Yaşım {} ve mesleğim {}.'.format(name,surname,age,job))
# 7) 'Hello world' ifadesindeki w harfini W ile değiştirin
variable='Hello world'
variable=variable[0:6]+'W'+variable[-4:]
variable.replace['w','W']#w gördüğün yere büyük W yaz
print(variable)

# 8) 'abc' ifadesini yan yana 3 defa yazdırın.
print('abc'*3)
