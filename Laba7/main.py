# Example for me

# class Tochka:
#   def __init__(self, x,y):
#     self.x = x 
#     self.y = y

#   def __str__(self):
#     return '(' + str(self.x) + ',' + str(self.y) + ')'

#   def __eq__(self, other):
#     if self.x == other.x and self.y == other.y:
#       return True
#     else:
#       return False
  
#   def __add__(self, other):
#     return Tochka(self.x + other.x, self.y + other.y)


# a = Tochka(2,3)
# b = Tochka(1,1)
# print(a)
# print(b)
# c = a+b
# print(c)
# print(a == b)

#########################################

# Task 1
import math 

class Vector:
  def __init__(self, x,y):
    self.x = x 
    self.y = y

  def __str__(self):
    return '(' + str(self.x) + ',' + str(self.y) + ')'

  def __eq__(self, other):
    if self.x == other.x and self.y == other.y:
      return True
    else:
      return False
  
  def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)

  def lenVector(x , y):
    return  math.sqrt(x * x + y * y)
    
  def scalarVector(self, other):
    return Vector(self.x * self.y + other.x * other.y)

a = Vector(2,3)
b = Vector(1,1)
print(a)
print(b)
c = a+b
print(c)
print(a == b)

len = Vector.lenVector(1,1)
print(len)

a = Vector(2,3)
b = Vector(1,1)
scalar = Vector.scalarVector(a,b)
print(scalar)

#########################################
