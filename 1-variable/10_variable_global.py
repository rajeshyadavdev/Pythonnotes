"""
Any variable created outside a function can be accessed within any function and so they have global scope.
"""
x = 12
y = 18

def sum():
  sum = x+y
  return sum

print(sum())#30