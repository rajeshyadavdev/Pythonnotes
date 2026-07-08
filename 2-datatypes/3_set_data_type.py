"""
Set is a Python implementation of set as defined in Mathematics. A set in Python is a collection, but is not an indexed or ordered collection as string, list or tuple. An object cannot appear more than once in a set, whereas in List and Tuple, same object can appear more than once.

Comma separated items in a set are put inside curly brackets or braces {}. Items in the set collection can be of different data types.
"""

set1 = {1,2.5,1+5j,"Rajesh"}
print(set1)

"""
A set can store only immutable objects such as number (int, float, complex or bool), string or tuple. If you try to put a list or a dictionary in the set collection, Python raises a TypeError.
"""
set2 = {['One', 'Two', 'Three'], 1,2,3, (1.0, 2.0, 3.0)}
print(set2)

