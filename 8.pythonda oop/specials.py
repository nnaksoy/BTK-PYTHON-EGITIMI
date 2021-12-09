#özel metodlar
myList=[1,2,3]
class Movie():
    def __init__(self,title,director,duraction):
        self.title=title
        self.director=director
        self.duraction=duraction
        print('movie objesi oluşturuldu.')
    def __str__(self):
        return f"{self.title} by {self.director}"
    def __len__(self):
        return self.duraction
m=Movie('film adı','yönetmen adı',120)
print(str(myList))
print(str(m))#normalde bu çalışmıyodu çünkü m clasının içinde bu metod yoktu. biz clasın içinde bunu kendine göre düzenledik ve kendi str metodunu çalıştırıyor artık
print(len(myList))
print(len(m))