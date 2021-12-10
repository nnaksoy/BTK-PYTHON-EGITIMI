#hata yönetimi
#güvenli kod yazmak için try-except komutları kullanılrır
while True:#while sayesinde yanlış oludğu sürece devam eder. doğru sonucu yani else girdiğinde whiledan çıkar
    try:
        x=int(input('x: '))
        y=int(input('y: '))
        print(x/y)
    #except (ZeroDivisionError,ValueError) as e: #oluşabilecek hataları buraya yazıyoruz. ve hata olduğunda burdaki mesajımız gözüküyor
    except Exception as e:#value zero errorlar exceptiondan türemiştir.genel olarak hepsini kapsar
        print('yanlış bilgi girdiniz')
        print(e)#hatanın türünü görmemizi sağlıyor
    else:#hata yoksa bu çalışır
        print('herşey yolunda')
        break
    finally:#else de olsa except te olsa her try exceptin çalışmasında çalışır.kaynakların kapatılması için değişkenlerin sonlandırılması için kullanılır.
        print('try except sonlandı')
