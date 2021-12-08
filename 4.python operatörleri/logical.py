x=5
result= 5<x<10
print(result)

#and mantıksal operatörü
#true,true->true
#true,false->false
result=(x>5) and (x<10)
print(result)

#or
#true,false->true
#true,true->true
#false,false->false
result=(x>0) or (x%2==0)
print(result)

#not
#tersini alma
result=not(x>0)
print(result)