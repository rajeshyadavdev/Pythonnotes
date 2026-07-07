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
print(c) #22.5

