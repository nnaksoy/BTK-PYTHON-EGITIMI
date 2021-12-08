## çoklu yorum satırı için 3 tırnak kullanılır
"""
1-bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.

müşteri adı
müşteri soyadı
müşteri ad+soyad
müşteri cinsiyet
müşteri tc kimlik
müşteri doğum yılı
müşteri adres bilgisi
müşteri yaşı

"""
from typing import OrderedDict


musteriAdi='Ali'
musteriSoyad='Yılmaz'
musteriAdSoyad=musteriAdi+' '+musteriSoyad
musteriCinsiyet=True #Erkek
musteriTcKimlik='13165465445'
musteriDogumYili=1989
musteriAdres='İstanbul Kadıköy'
musteriYasi=2019-musteriDogumYili
print(musteriYasi)

"""
2- aşağıdaki siparişlerin toplam bilgisini hesaplayınız.

sipariş 1=> 110 tl
sipariş 2=>1100.5 tl
sipariş 3=>356.95 tl

"""
order1=110 
order2=1100.5
order3=356.95
total=order1+order2+order3
print("Total: ",total)
