#There are three numeric types in Python:
# int
# float
# complex

#when dividing using single /, it does floating point division
#and with double //, it does integer division
var1 = 14
var2 = 10
res1 = var1 / var2
res2 = var1 // var2
print(f'var1 / var2 = {res1}')
print(f'var1 // var2 = {res2}')

#float as scientific number
x = 10e5 #100000
print(x)
print(int(x))

#complex numbers

a = 4 + 7j
b = 3 + 1j
print(f'Sum = {a+b}')
print(f'Difference = {a-b}')
print(f'Product = {a*b}')
print(f'Division = {a/b}')

