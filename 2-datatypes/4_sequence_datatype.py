"""
Sequence is a collection data type. It is an ordered collection of items. Items in the sequence have a positional index starting with 0. It is conceptually similar to an array in C or C++. There are following three sequence data types defined in Python.

List Data Type
Tuple Data Type
Range Data Type

Python sequences are bounded and iterable - Whenever we say an iterable in Python, it means a sequence data type
"""

list1 = [1,2,3,4]

tuple1 = (1,2,3,4)

"""
A Python range is an immutable sequence of numbers which is typically used to iterate through a specific number of items.

It is represented by the Range class. The constructor of this class accepts a sequence of numbers starting from 0 and increments to 1 until it reaches a specified number. 
"""

# range(start,stop,step)

"""
start: Integer number to specify starting position, (Its optional, Default: 0)

stop: Integer number to specify ending position (It's mandatory)

step: Integer number to specify increment, (Its optional, Default: 1)
"""

# 5 is stop argument,print 0 to 4
for i in range(5):
  print(i)

# 2 is start, 5 is end, its start with 2 and end at 4
for i in range(2,5):
  print(i)

# start 2, end 10,step 2, so the output is 2,4,6,8
for i in range(2,10,2):
  print(i)

str1 = "Rajesh is a software developer"
str2 = 'Rajesh code in python language'