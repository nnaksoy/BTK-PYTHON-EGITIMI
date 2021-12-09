#global ve local değişkenler
x='global x'
def function():
    x='local x'
    print(x)

function()
print(x)
####################################
name='çınar'
def changeName(new_name):
    name=new_name
    print(name)

changeName('ada')
print(name)
####################################
name='global string'
def greeting():
    name='çınar'
    def hello():
        print('hello '+name)#bir üstündeki değişkeni kullanır. çınarı alır
    hello()

greeting()

#normal şartlarda global bi değişkeni fonksiyon içinde yeni değer atanınca o değer sadece fonksiyon içinde kalır. global olarak değişmez. eğer global olarak değerinin değişmesini istiyosan:global x şeklinde yaz fonksiyonun içinde yaptığın tüm değişimler xte glonbal olarak geçerli olur