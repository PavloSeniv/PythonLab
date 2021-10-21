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

#Task 1
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
    print('Даний вектор для знаходження довжини','(' + str(x) + ',' + str(y) + ')')
    return  math.sqrt(x * x + y * y)
    
  def scalarVector(self, other):
    self_var = self.x * self.y 
    other_var = other.x * other.y
    result_sum = self_var + other_var
    return result_sum

a = Vector(2,3)
b = Vector(1,1)
print("Вектор 1:",a)
print("Вектор 2:",b)

c = a+b
print("Вектор 3 (Додавання вектора 1 та 2):",c)

print("Перевірка на рівність 1 та 2 вектора:", a == b)

len = Vector.lenVector(11,13)
print("Довжина вектора:",len)

a = Vector(2,3)
b = Vector(1,1)
scalar = Vector.scalarVector(a,b)
print("Скалярний добуток вектора " + str(a) + " та вектора " + str(b) + " дорівнює ",scalar)

#########################################
# Task 2

# class Student:
#   def __init__(self, surname, name, subject ):
#     self.surname= surname
#     self.name = name
#     self.subject = subject
    
#   def __str__(self):
#     return 'Student: ' + self.surname + " " + self.name + ". " + "Предмети: " + str(self.subject)

#   def pointSubject(self, points):
#         return self.subject[points]

# stud_seniv = Student('Seniv', 'Pavlo', {"TAML":[4, 5, 4, 5, 4], "C#":[5, 3, 3]})
# print(stud_seniv)

# print("TAML:" + str(stud_seniv.pointSubject("TAML")))

#########################################

# Task 3
# class Iteration:
#   def __init__(self,number,step,end):
#     self.number = number
#     print(self.number)
#     self.step=step
#     self.end=end
#   def __iter__(self):
#     return self
#   def __next__(self):
#     if self.number>=self.end:
#       raise StopIteration
#     self.number = self.number + self.step
#     if self.number>self.end:
#       raise StopIteration
#     return self.number


# d=Iteration(0,2,18) # Початок, крок, кінець проміжку
# for i in d:
#   print(i)

#########################################
