"""
Python identity operators compare the memory locations of two objects.

There are two Identity operators explained below −
"""

"""
is	
Returns True if both variables are the same object and false otherwise.	
a is b

is not	
Returns True if both variables are not the same object and false otherwise.
"""
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = a

print(a is c)
print(a is b)

print(a is not c)
print(a is not b)
