"""
Python Comparison operators compare the values on either side of them and decide the relation among them. They are also called Relational operators.
"""
a = 10
b = 20

# == Equal
print(f"{a}=={b}:{(a==b)}")# False

# != not equal
print(f"{a}=={b}:{(a!=b)}")# True

# > greater than
print(f"{a}>{b}:{(a>b)}")# False

# < less than
print(f"{a}<{b}:{(a<b)}")# True

# >= greater than equal
print(f"{a}>={b}:{(a>=b)}")# False

# <= less than equal
print(f"{a}<={b}:{(a<=b)}")# True


age = 25

if(age>=18):
  print("You can vote.")
else:
  print("You cannot vote.")



