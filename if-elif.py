num=int(input('sayı: '))
if num>0:
    print('sayı pozitif')
elif num==0:
    print('sayi 0 dır')
else:
    print('sayı negatiftir')

#ÖRNEK
import datetime
tarih=input('tarih giriniz(2019/8/9): ')
tarih=tarih.split('/')
simdi=datetime.datetime.now()
trafigecikis=datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
fark=simdi-trafigecikis
print(fark.days)