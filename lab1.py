# task 1 - 4
# task1X = int(input())
# print('1: ' + str(task1X))
# task1X = float(task1X + 0.8)
# print('2: ' + str(task1X))
# task1X = str(task1X)*3
# print('3: ' + str(task1X))

# task 5
# n = int(input())
# ivEnding = ['0', '6', '7', '8','9']
# aEnding = ['2', '3', '4']
# zeroEnding = ['1']
# if n >= 100:
#   print('Number is greater than 100')
# elif str(n)[-1] in ivEnding:
#   print('Zalik zdalo ' + str(n) + ' studentiv')
# elif str(n)[-1] in aEnding:
#   print('Zalik zdalo ' + str(n) + ' studenta')
# elif str(n)[-1] in zeroEnding:
#   print('Zalik zdalo ' + str(n) + ' student')

# task 8
# def isSimple(n):
#     if n % 2 == 0:
#         return n == 2
#     nextN = 3
#     while nextN * nextN <= n and n % nextN != 0:
#         nextN += 2
#     return nextN * nextN > n

# print(isSimple(1))
# print(isSimple(3))
# print(isSimple(8))
# print(isSimple(6))

#task 9
# import random
# randomlist = []
# for i in range(0,10):
#   randomlist.append(random.randint(1,50))
# print(randomlist)

#task 10
# import random
# isRun = True
# while(isRun):
#   a = random.randint(1,10)
#   b = random.randint(1,10)
#   print(f'Please enter a result of: {a}*{b}')
#   userInp = int(input())
#   if userInp == a * b:
#     print('Now you are free....')
#     isRun = False
#   else:
#     print('Wrong answer. Try again...')

#task exception 1
# try:
#   x = int(input())
#   result = 1/x
# except ZeroDivisionError:
#   print('you cant divide by zero')
# finally:
#   print('Good bye')

#task ex 2
# import random

# myList = None

# def createList():
#   global myList
#   myList = []

# def addElement():
#   print('Element: ')
#   try:
#     el = int(input())
#     myList.append(el)
#   except ValueError:
#     print('Incorrect value entered. Please enter a number')
#   except AttributeError:
#     print('You should create a list before inserting')

# def preview():
#   print(myList)
 
# def createAuto():
#   global myList
#   print('Please specify a size of list')
#   r = int(input())
#   myList = random.sample(range(10, 30), r)

# def removeByIndex():
#   global myList
#   print('Please specify an index (starting from 1)')
#   myList.pop(int(input())-1)

# while True:
#   print('My menu')
#   print('1: create list')
#   print('2: add element')
#   print('3: preview')
#   print('4: exit')
#   print('5: create a list automatically')
#   print('6: remove element by index')
#   inp = int(input())
#   if inp == 1:
#     createList()
#   elif inp == 2:
#     addElement()
#   elif inp == 3:
#     preview()
#   elif inp == 4:
#     break
#   elif inp == 5:
#     createAuto()
#   elif inp == 6:
#     removeByIndex()
#   elif inp > 6:
#     print('It is not a menu item')



