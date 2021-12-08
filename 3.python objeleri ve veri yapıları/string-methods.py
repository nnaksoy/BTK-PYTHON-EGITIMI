message='Hello There. My name is Sadık Turan'
message=message.upper()#bütün karakterleri büyük harfe çevirir
message=message.lower()# bütün karakterleri küçük harfe çevirir
message=message.title()# her kelimenin ilk harfini büyük harfe çevirir.
message=message.capitalize()#verilen ifadenin sadece ilk harfini büyük geri kalanı küçük yapar
message=message.strip()#baş ve sondaki boşluğu siler.sadece soldan silme lstrip sadece sağdan silme rstrip
#belirli karakterleri silme: website.lstrip('/:pth')
message=message.split()#değişkeni parçalara ayrır.splite bişe belirtmedikçe boşluktan ayırır
print(message)
print(message[2])
message=' '.join(message)#birleştirme yapar. parçaların arasına boşluk ekler
message='Hello There. My name is Sadık Turan'
index=message.find('Sadık')#string içinde var mı yok mu die aramak istediğimiz şeyi yazıyıruz ve bize bulunduğu ilk indisi döndüryo. eğer yoksa - li sayı gelr
print(index)
isFound=message.startswith('H')
# h ile başlıyosa true döndrür
print(isFound)
isFound=message.endswith('n')
print(isFound)
message=message.replace('Sadık','Çınar')#bulup diğeriyle değiştirir
print(message)
"""
mesela birşeyde türkçe karakterleri değiştirmek istersek
message=message.replace('ç','c').replace('ü','u').replace('ö','o')
"""
#message=message.center(100)#100 karakterlik alanın ortasına yerleştirir
message=message.center(50,'*')#50 karakterlik alanın sağı ve soluna * ekle
print(message)

message=message.count('a')# kaç tane a var sayısını döndürür
message=message.count('a',0,10)#0 ve 10. indisler arasındaki sayısını verir
#course.isalpha()-> tüm karakterler harfse true değeri verir. course.isdigit()-> tüm karakterler rakamsa true değeri verir