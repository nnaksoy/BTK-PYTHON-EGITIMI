def sayHello(name='user'):#def fonksiyon tanımlaması sayhello fonksiyon adı
    #parametreyi bu şekilde tanımladığımızda fonksiyonu çağırırken birşey göndermezsek hata vermez ve varsayılan olarak eşitdeğimiz değeri atar.
    return 'hello '+name#sayhello dan bir değer döndürme

message=sayHello('ahsen')
print(message)

def total(num1,num2):
    return num1+num2

result=total(10,20)
print(result)