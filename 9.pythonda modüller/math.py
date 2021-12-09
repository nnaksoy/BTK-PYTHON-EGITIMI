#hazır modül kullanma
#YÖNTEM 1

#import math-> bu hazır kütüphaneye takma isim koyarak o ismi kullanabilirz
#import math as islem
#value=dir(math)#math modulunun içerdikleri.isimleri hakkında bilgi sahibi olmak için
#value=help(math)#ayrıntılı bilgi verir

#YÖNTEM 2
from math  import *#math kütüphanesinden tüm metodları import et demek. artık içindekileri kullanmak için her defasında math üzerinden çağırmaya gerek kalmaz
def sqrt(x):
    print('x: '+str(x))# en son hangi metod tanımlanmışsa onu kullanır. math i kullanmadı bunu kullandı. eğer bu fonksiyonu from math den önce koyarsan math dekini kullanır
value=sqrt(49)
print(value)