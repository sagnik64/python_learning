#Function for printing type and value of var
def print_with_type(var):
    print(f'type = {type(var)}, value = {var}')


#Python has the following built-in data types:


#Numeric Types: int, float and complex

int1 = 10
print_with_type(int1)

float1 = 10.5
print_with_type(float1)

complex1 = 10j
print_with_type(complex1)
print()


#Text Type: str

str1 = "programming"
print_with_type(str1)
print()


#Sequence Types: list, tuple and range

list1 = [1,2,5,10,8]
print_with_type(list1)

tuple1 = (1,2,4,7,20,10)
print_with_type(tuple1)

range1 = range(5)
print_with_type(range1)


#Mapping Type: dict

dict1 = {'a': 5, 'b': 10, 'c': 7}
print_with_type(dict1)
print()


#Set Type: set

set1 = {4, 8, 9, 25, 15, 12, 8, 9, 9, 10}
print_with_type(set1)
print()

#Boolean Type: bool

bool1 = True
print_with_type(bool1)
print()


#None Type: None
a = None
print_with_type(a)