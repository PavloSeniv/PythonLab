<<<<<<< HEAD
# Example for me

# class Person:
#     def __init__(self, name, job=None, pay=0):
#         self.name = name
#         self.job = job
#         self.pay = pay
#     def giveRaise(self, graise):
#         self.pay=graise

# class Manager(Person):
#     def __init__(self, name, pay=1000):
#         Person.__init__(self, name, 'mgr', pay)
#     def giveRaise(self, graise, bonus=100):
#         Person.giveRaise(self, graise + bonus)

#Task 1
import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def calcPerimeter(self):
         return self.a + self.b + self.c
    def calcArea(self, h):
        return 0.5 * self.a * h

class Isosceles(Triangle):
    def __init__(self, a, b, c=None):
        Triangle.__init__(self, a, b, c=None)
    def calcPerimeter(self):
        return 2*self.a + self.b
    def calcArea(self):
        return 0.5 * self.a * self.a

class Equilateral(Triangle):
    def __init__(self, a, b=None, c=None,):
        Triangle.__init__(self, a, b=None, c=None,)
    def calcPerimeter(self):
        return 3*self.a
    def calcArea(self):
        return self.a * self.a * math.sqrt(3)/4

triangle = Triangle(10,20,30)
print("Сторони трикутника:", "a=" + str(triangle.a), "b=" + str(triangle.b), "c=" + str(triangle.c))
print("Периметр трикутника:", triangle.calcPerimeter())
print("Площа трикутника:", triangle.calcArea(5))
print("-------------------------------------")

isosceles_triangle = Isosceles(10,20,30)
print("Сторони рівнобедреного трикутника:", "a=" + str(isosceles_triangle.a), "b=" + str(isosceles_triangle.b), "c=" + str(isosceles_triangle.c))
print("Периметр рівнобедреного трикутника:", isosceles_triangle.calcPerimeter())
print("Площа рівнобедреного трикутника:", isosceles_triangle.calcArea())
print("-------------------------------------")

equilateral_triangle = Equilateral(10,20,30)
print("Сторони рівностороннього трикутника:", "a=" + str(equilateral_triangle.a), "b=" + str(equilateral_triangle.b), "c=" + str(equilateral_triangle.c))
print("Периметр рівностороннього трикутника:", equilateral_triangle.calcPerimeter())
print("Площа рівностороннього трикутника:", int(equilateral_triangle.calcArea()))

#########################################

#Task 2
# import requests
# import json

# danni = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
# obmin = json.loads(danni.text)
# print(obmin)

# class Pryvat:
#   def dani(self):
#     d=requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
#     return d.json()

# class EUR(Pryvat):
#   def __init__(self,a):
#     self.a = a
#   def convert_to_uah(self):
#     return self.a*float(obmin[1]['sale'])
#   def convert_to_usd(self):
#     return self.a*float(obmin[1]['sale'])/float(obmin[0]['buy'])

# class USD(Pryvat):
#   def __init__(self,a):
#     self.a = a
#   def convert_to_eur(self):
#     return self.a*float(obmin[0]['sale'])/float(obmin[1]['buy'])
#   def convert_to_uah(self):
#     return self.a*float(obmin[0]['sale'])

# class BTC(Pryvat):
#   def __init__(self,a):
#     self.a = a
#   def convert_to_uah(self):
#     return self.a*float(obmin[3]['sale'])
#   def convert_to_usd(self):
#     return self.a*float(obmin[3]['sale'])/float(obmin[0]['buy'])

# a= Pryvat()

# print("-------------------------------------")
# money=EUR(100)
# print(str(money.a) + " євро - це " + str(money.convert_to_uah()) + " 'гривень' ")
# print(str(money.a) + " євро - це " , int(money.convert_to_usd()) , " доларів ")
# print("-------------------------------------")

# money=USD(100)
# print(str(money.a) + " доларів - це " , int(money.convert_to_eur()) , " євро ")
# print(str(money.a) + " доларів - це " , int(money.convert_to_uah()) , " гривень ")
# print("-------------------------------------")

# money=BTC(100)
# print(str(money.a) + " біткойнів - це " , int(money.convert_to_uah()) , " гривень ")
# print(str(money.a) + " біткойнів - це " , int(money.convert_to_usd()) , " доларів ")
# print("-------------------------------------")

#########################################

#Task 3
# class Student:
#   def __init__(self, name, zalik):
#     self.name= name
#     self.__zalik = zalik

#   @property
#   def zalik(self):
#     return self.__zalik

#   @zalik.setter
#   def zalik(self, zalik):
#     if zalik >= 50 | zalik <=100 :
#       print("зарах")
#     elif zalik > 100:
#       print("неправильний бал")
#     else:
#       print("незарах")

# stud = Student("Seniv", 50)
# print(stud.name, stud.zalik)
# stud.zalik = 50

#########################################
>>>>>>> 22b019313540c418e639a75e9c6ed1a7caa9351a
