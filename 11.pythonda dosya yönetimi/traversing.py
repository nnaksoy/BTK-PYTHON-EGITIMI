#dosya okuma fonksiyonları
# file=open("newfile.txt","r",encoding="utf-8")
# content=file.read()
# print(content)
# file.close()

from typing import ContextManager


with open("newfile.txt","r",encoding="utf-8") as file:
    content=file.read()
    print(content)
    file.seek(0)#imleci istediği konuma gönderir
    print(file.tell())#o anki imlecin konumu verir
#close metoduna gerek kalmıyor. with ile açtığımız kod bloğun sonunda dosya kendisi kapanıyor