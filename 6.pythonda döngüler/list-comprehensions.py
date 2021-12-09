numbers=[x for x in range(10)]
print(numbers)

numbers=[x**2 for x in range(10)]
print(numbers)

numbers=[x*x for x in range(10) if x%3==0]
print(numbers)

mystring='hello'
myList=[letter for letter in mystring]
print(myList)

years=[1983,1999,2008,1956,1986]
ages=[2019-year for year in years]
print(ages)

numbers=[(x,y) for x in range(3) for y in range(3)]
print(numbers)