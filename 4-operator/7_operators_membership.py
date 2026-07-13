"""
Python's membership operators test for membership in a sequence, such as strings, lists, or tuples.
"""
"""
in
Returns True if it finds a variable in the specified sequence, false otherwise.
a in b

a not in b
not in	returns True if it does not finds a variable in the specified sequence and false otherwise.
"""
a = 10
b = 20
list = [1, 2, 3, 4, 5 ]

print ("a:", a, "b:", b, "list:", list)

if ( a in list ):
   print ("a is present in the given list")
else:
   print ("a is not present in the given list")

if ( b not in list ):
   print ("b is not present in the given list")
else:
   print ("b is present in the given list")

c=b/a
print ("c:", c, "list:", list)
if ( c in list ):
   print ("c is available in the given list")
else:
    print ("c is not available in the given list")