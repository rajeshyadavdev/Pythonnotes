"""
Implicit (Automatic): 
Python safely converts types during math to prevent data loss.
​Example: 10 + 5.5 becomes 15.5 (float).

​Explicit (Manual): 
Forcing a type change using constructor functions:
​int("10") # 10
​float(5) # 5.0
​str(100) # "100"
​bool(1) # True
"""
"""
Float-to-Int Truncates: 
int(9.99) becomes 9 (it chops off the decimal; it does not round up).

​No Math with Strings: 
"5" + 5 causes a TypeError. You must explicitly cast first: int("5") + 5.

​Falsy Values: 
When using bool(), only 0, 0.0, empty strings "", empty lists [], and None convert to False. Almost everything else is True.
"""

a = 12
b = 10.5
c = a+b
print(type(c),c) #22.5

age = 23
int_to_str = str(age)
print(type(int_to_str),int_to_str)
# "23"

int_to_float = float(age)
print(type(int_to_float),int_to_float) #23.0

name = "Rajesh"
# we must use base 10 means number
#int_name = int(name) 

num_str = "12"
str_to_int = int(num_str)
print(type(str_to_int),str_to_int)#12

str_to_float = float(num_str)
print(type(str_to_float),str_to_float)
#12.0

float_num = 23.6
float_to_int = int(float_num)
print(type(float_to_int),float_to_int)
#23
float_to_str = str(float_num)
print(type(float_to_str),float_to_str)
# "23.6"

print(type(bool(0)),bool(0))#False
print(type(bool(1)),bool(1))#True

print(type(bool(" ")),bool(" "))#True

print(type(bool("")),bool(""))#False

print(type(bool({"id":1})),bool({"id":1}))#True
print(type(bool({})),bool({}))#False

print(type(bool([])),bool([]))#False
print(type(bool([1])),bool([1]))#True

print(type(bool(())),bool(()))#False
print(type(bool((1,))),bool((1,)))
#True

print(type(bool(0.0)),bool((0.0)))
#False
print(type(bool(0.2)),bool((0.2)))
#True

print(type(bool(None)),bool((None)))
#False




