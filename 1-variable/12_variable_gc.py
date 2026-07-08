"""
Python's garbage collector mechanism releases the memory occupied by any unreferred object.

Python's identity operator is returns True if both the operands have same id() value.
"""

a = 10
b = 10
print(a is b) #True
print(id(a) is id(b)) #False
print(id(a),id(b)) #both will be same


x = y = 20
print(x is y) #True
print(id(x) is id(y)) #False
print(id(x),id(y)) #both will be same
