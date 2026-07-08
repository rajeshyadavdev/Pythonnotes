"""
Python allows to initialize more than one variables in a single statement. In the following case, three variables have same value.
"""
a = 10
b = 10
c = 10

"""
Instead of separate assignments, you can do it in a single assignment statement as follows −
"""
a=b=c = 10
print(a,b,c) #10 10 10

# we have three variables with different values.

a = 10
b = 20
c = 30

#These separate assignment statements can be combined in one. 

a,b,c = 10,20,30
print(a,b,c) #10 20 30

name, age, amount = "Rajesh",20,100.50
print(name,age,amount)
