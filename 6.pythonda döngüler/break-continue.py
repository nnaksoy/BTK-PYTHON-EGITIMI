name='Sadık Turan'
for letter in name:
    if letter=='a':
        break #döngüden tamamen çıkar
    print(letter)
print('********************')
for letter in name:
    if letter=='a':
        continue#o an ki turu çıkar ve döngü devam eder
    print(letter)