"""
When any language compiler/interpreter automatically converts object of one type into other, it is called automatic or implicit casting. Python is a strongly typed language. It doesn't allow automatic type conversion between unrelated data types. For example, a string cannot be converted to any number type. However, an integer can be cast into a float. Other languages such as JavaScript is a weakly typed language, where an integer is coerced into a string for concatenation.
"""

"""
Note that memory requirement of each data type is different. For example, an integer object in Python occupies 4 bytes of memory, while a float object needs 8 bytes because of its fractional part. Hence, Python interpreter doesn't automatically convert a float to int, because it will result in loss of data. On the other hand, int can be easily converted into float by setting its fractional part to 0.
"""

a = 10 #int type
b = 10.5 #float type
c = a+b 
print(type(c),c) #20.5


"""
In implicit type casting, a Python object with lesser byte size is upgraded to match the bigger byte size of other object in the operation. For example, a Boolean object is first upgraded to int and then to float, before the addition with a floating point object. In the following example, we try to add a Boolean object in a float, pleae note that True is equal to 1, and False is equal to 0.
"""

float_var = 10.5
boolean_var = True

sum = float_var + boolean_var

print(type(sum),sum) #11.5


