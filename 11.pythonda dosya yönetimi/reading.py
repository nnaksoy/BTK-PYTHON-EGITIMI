# try:
#     file=open("newfile.txt","r")
#     print(file)
# except FileNotFoundError:
#     print('dosya okuma hatası')
# finally:
#     print('dosya apandı.')
#     file.close()

from functools import partialmethod
from typing import ContextManager


file=open("newfile.txt","r",encoding="utf-8")

# #for döngüsü ile okuma:
# for i in file:
#     print(i, end="")#boş satır eklemeden devam et->end


#read() fonksiyonu ile okuma
# content=file.read()
# print(content)

# content=file.read(5)#ilk 5 karakteri alır
# print(content)
# content=file.read(3)#kaldığı yerden devam eder
# print(content)

#readline() fonksiyonu
#her seferinde bir satır okur
# print(file.readline(),end="")
# print(file.readline(),end="")#satır satır. kaldığı yerden devam eder
# print(file.readline(),end="")

#readlines() fonksiyonu
liste=file.readlines()#her satır bilgisini listeye eleman olarak atar
print(liste)


file.close()
