# set 
numbers = {1,3,5,7,9,66,55,44,33,22,11}
numbers.add(77)
print(numbers)
numbers.remove(66)

for i in numbers:
    print(i)
    
def check_number(num):
    return num in numbers   
print(check_number(3))
print(check_number(10))

#frozenset
#immutable
numbers = frozenset({1,3,5,7,9,66,55,44,33,22,11})
print(numbers)


