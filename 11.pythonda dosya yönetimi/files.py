#dosya açmak ve oluşturmak için open() fonksiyonu kullnılır
#open kullanımı-> open(dosya_adi,dosya_erişme_modu)

#"w":write. yazma modu.dosyayı konumda oluşturur.dosya içeriğini diler ve yeniden ekleme yapar.
# file=open("newfile.txt","w")#result üzerinden dosyayla ilgili işlemler yapçaz. result opendan dönen parametreyi saklar
# print(file)
# file.close()#açtığımız dosyayı kapatır.

# file=open("C:/users/nisan/desktop/newfile.txt","w")
# print(file)

# file=open("newfile.txt","w",encoding='utf-8')#w modu bi dosyayı tekrar açtığında içindeki bilgileri siler öyle başlar.utf-8 türkçe karakteri algılaması için
# file.write('sadık turan')
# file.close()


#"a":append.ekleme. dosya konumda yoksa oluşturur.var olan içeriği silmez sonuna ekleme yapar.
# file=open("newfile.txt","a",encoding='utf-8')
# file.write(' sadık turan')
# file.close()


#"x":crete. oluşturma. dosya zaten varsa hata verir.
#sadece oluşturur okuma yazma yapmaz

#"r":read. okuma. varsayılan dosya konumda yoksa hata verir