"""
The int() function returns an integer from a string object, only if it contains a valid integer representation.
"""

str_var = "1234"
int_var = int(str_var)
print(type(int_var),int_var)#1234

a = ("10"+"10")
print(type(a),a) #"1010"

b = int(a)
print(type(b),b)#1010


"""
However, if the string contains a non-integer representation, Python raises ValueError.
"""

x = "10.5"
y = int(x)#ValueError

p = "Rajesh Yadav"
q = int(p)#ValueError

"""
The int() function also returns integer from binary, octal and hexa-decimal string. For this, the function needs a base parameter which must be 2, 8 or 16 respectively. The string should have a valid binary/octal/Hexa-decimal representation.

Binary String to Integer
The string should be made up of 1 and 0 only, and the base should be 2.
"""


