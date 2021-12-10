#dosyada güncelleme işlemleri


# with open("newfile.txt","r+",encoding="utf-8") as file:#r+ hem okuma hem yazma yapar. bunla en başa ekleme yapar r modunda olduğu için w yazarken en baştan başlıyodu çünkü
#     file.seek(20)#istediğimiz konuma ekleme yapma
#     file.write("deneme")

# with open("newfile.txt","r+",encoding="utf-8") as file:#r+ hem okuma hem yazma yapar
#     print(file.read())

#sayfa sonundan güncelleme

# with open("newfile.txt","a",encoding="utf-8") as file:
#     #append ekleme işlemi yapar. imleç sondan başlar
#     file.write("\nemel turan")

# with open("newfile.txt","r",encoding="utf-8") as file:
#      print(file.read())

#sayfa başından güncelleme

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     content=file.read()
#     content="efe turan\n"+content
#     file.seek(0)
#     file.write(content)
# with open("newfile.txt","r",encoding="utf-8") as file:
#       print(file.read())

#sayfa ortasında güncelleme
with open("newfile.txt","r+",encoding="utf-8") as file:
    liste=file.readlines()
    liste.insert(1,"yılmaz korkmaz\n")#insert verdiğimiz index numarasından önce ekleme yapar
    file.seek(0)
    # for i in liste:
    #     file.write(i)
    file.writelines(liste)#forla tek tek yazmak yerine liste şeklinde yazdık
with open("newfile.txt","r",encoding="utf-8") as file:
      print(file.read())