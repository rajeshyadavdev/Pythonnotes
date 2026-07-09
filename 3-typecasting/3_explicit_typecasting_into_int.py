"""
Although automatic or implicit casting is limited to int to float conversion, you can use Python's built-in functions int(), float() and str() to perform the explicit conversions such as string to integer.
"""

# int() function
int_var = 10
print(type(int_var),int_var) #10

float_var = 10.5
float_to_int = int(int_var)
print(type(float_to_int),float_to_int)#10


"""
If the argument to int() function is a float object or floating point expression, it returns an int object.
"""
print(int(2*12.5)) #25

"""
The int() function also returns integer 1 if a Boolean object is given as argument
"""
is_raining = True # True means 1
age = 10
sum = int(age + is_raining)
print(sum) #11


