#bir fonksiyona bir özellik eklemek için
#bir özelliği birden fazla fonksiyonla ilişkilendirmek için kullanılır.

def my_decorator(func):
    def wrapper(name):
        print("fonksiyondan önce olan işlemler")#gönderilen fonksiyonun çalışmasından önce çalışan özellikler
        func(name)
        print("fonksiyondan sonraki işlemler")
    return wrapper

@my_decorator#sayhello=my_decorator(sayhello) bu işlemi yapar
def sayhello(name):
    print("hello ",name)

def sayGreeting():
    print("greeting")

# sayhello=my_decorator(sayhello)
# sayhello()
#aynı özelliği greeting e de eklemek istersek kolayca ekleyebilirz.

sayhello("ali")


import math
import time
from typing import Callable
def calculate_time(func):
    def inner(*args,**kwargs):
        start=time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish=time.time()
        print(f"fonksiyon {func.__name__} {finish-start} saniye sürdü")
    return inner
@calculate_time
def usalma(a,b):
    print(math.pow(a,b))
    
@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

usalma(2,5)
faktoriyel(4)