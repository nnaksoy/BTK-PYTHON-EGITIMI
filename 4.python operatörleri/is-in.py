#   Identity Operator: is
# değerlerini değil objelerin aynı olup olmadığı yani adreslerini karşılaştırır
x=y=[1,2,3]
z=[1,2,3]
print(x==y)
print(x==z)
print(x is y)
print(x is z)

a=[1,2]
b=[1,2]
print(a is b)

# membership operator: in
# içinde olup olmadığı sorgulanır. yok mu diye sorgulama->>not in
x=['apple','banana']
print('banana' in x)