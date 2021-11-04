<<<<<<< HEAD
# Task1
# set_number = set(input().split()) # Приклад вхідних даних: 1 2 3 4 5 6 7 або 7 7 6 6 4 4 3 2 1
# # print(set_number)

# number_list = len(set_number) 
# print(number_list)

# a = list(set_number)

# number_list_sort = sorted(a)
# print(number_list_sort)


# Task3
# def check(string):
#     # brackets_open = ('(', '[', '{', '<')
#     # brackets_closed = (')', ']', '}', '>')
#     brackets_open = ('(')
#     brackets_closed = (')')
#     stack = []
#     for i in string:
#         if i in brackets_open:
#             stack.append(i)
#         if i in brackets_closed:    
#             if len(stack) == 0:
#                 return False
#             index = brackets_closed.index(i)
#             open_bracket = brackets_open[index]
#             if stack[-1] == open_bracket:
#               stack = stack[:-1] 
#             else:
#               return False   
#     return (not stack)

# str1 = 'Сенів павло(аввав), аовао(вава), аваовао(па)' 
# print(check(str1))

# Task T13.1
# class Person:
#   def __init__(self):
#     self.name = None
#     self.byyer = None

#   def input(self):
#     self.name = input('Прізвище: ')
#     self.byyer = input('Рік народження: ')

#   def print(self):
#     print(self.name, self.byyer, end = ' ', )

# class Friend(Person):
#   def __init__(self):
#     self.tel = None

#   def input(self):
#     self.name = input('Прізвище: ')
#     self.byyer = input('Рік народження: ')
#     self.tel = input('Номер телефону: ')

#   def print(self):
#     print(self.name, self.byyer, self.tel, end = '')

# person = Person()
# person.input()
# person.print()

# print("\n" + "------------------------")

# friend = Friend()
# friend.input()
# friend_date = friend.print()

# print("\n" + "------------------------")

# print("My dovidnuk")
# print("1: create dovidnuk")
# print("2: add friend")
# print("3: preview")
# print("4: exit")
# print("5: find tel for surname")
# print("6: save in file")
# print("7: read in file")

# while True:
#     try:
#         number_menu = int(input("Ваші дії: "))
#         if number_menu == 1:
#             list_a = []
#             print("Done")
#         if number_menu == 2:
#             try:
#                 friend = Friend()
#                 friend.input()
#                 element_a = [friend.name, friend.byyer, friend.tel]
#                 list_a.append(element_a)
#             except:
#                 print("Створіть спочатку список")
#         if number_menu == 3:
#             try:
#                 print(list_a)
#             except:
#                 print("Створіть спочатку список")
#         if number_menu == 4:
#             break
#         if number_menu == 5:
#             finder_surname = input('Введіть прізвище: ')
#             for item_list in list_a:
#               # print(item)
#               for item_set in item_list:
#                 if finder_surname == item_set:
#                   print("Прізвище", item_set, "знайдено")
#                   item_set_new_tel = input('Новий номер телефону: ')
#                   # print(item_list[2])
#                   item_list[2] = item_set_new_tel
#                   # print(item_list[2])
#         if number_menu == 6:
#           with open("dictFriend.txt", "w") as file:
#             file.write(str(list_a))
#           print("Довідник записано у файл")
#         if number_menu == 7:
#           print("Довідник виведено з файлу")
#           with open("dictFriend.txt", "r") as file:
#             for line in file:
#               print(line)
#         if number_menu > 8:
#           print("Немає такої категорії меню")        
#     except ValueError:
#         print("Необхідно задати число!")

# Task T13.2
# class Person:
#   def __init__(self):
#     self.name = None
#     self.byyer = None

#   def input(self):
#     self.name = input('Прізвище: ')
#     self.byyer = input('Рік народження: ')

#   def print(self):
#     print(self.name, self.byyer, end = ' ', )

# class Employee(Person):
#   def __init__(self):
#     self.registration_number = None
#     self.wages = None

#   def input(self):
#     self.name = input('Прізвище: ')
#     self.byyer = input('Рік народження: ')
#     self.registration_number = input('Табельний номер: ')
#     self.wages = input('ЗП за місяць: ')

#   def print(self):
#     print(self.name, self.byyer, self.registration_number, self.wages, end = '')

# person = Person()
# person.input()
# person.print()

# print("\n" + "------------------------")

# employee = Employee()
# employee.input()
# friend_date = employee.print()

# print("\n" + "------------------------")

# while True:
#     try:
#         number_menu = int(input("Ваші дії: "))
#         if number_menu == 1:
#             list_a = []
#             print("Done")
#         if number_menu == 2:
#             try:
#                 employee = Employee()
#                 employee.input()
#                 element_a = [employee.name, employee.byyer, employee.registration_number, employee.wages]
#                 list_a.append(element_a)
#             except:
#                 print("Створіть спочатку список")
#         if number_menu == 3:
#             try:
#                 print(list_a)
#             except:
#                 print("Створіть спочатку список")
#         if number_menu == 4:
#             break
#         if number_menu == 5:
#             finder_surname = input('Введіть прізвище: ')
#             for item_list in list_a:
#               # print(item)
#               for item_set in item_list:
#                 if finder_surname == item_set:
#                   print("Робітника", item_set, "знайдено")
#                   hours_per_month = 240
#                   if int(item_list[2]) >= int(hours_per_month):
#                     item_list[3] = str(int(item_list[2]) * int(item_list[3]))
#                     print("Середня зарплата", item_list[3])
#                   else:
#                     print("Потрібно відпрацювати мінімум", hours_per_month)
#         if number_menu == 6:
#           with open("dictEmployee.txt", "w") as file:
#             file.write(str(list_a))
#           print("Довідник записано у файл")
#         if number_menu == 7:
#           print("Довідник виведено з файлу")
#           with open("dictEmployee.txt", "r") as file:
#             for line in file:
#               print(line)
#         if number_menu > 8:
#           print("Немає такої категорії меню")        
#     except ValueError:
#         print("Необхідно задати число!")

>>>>>>> 22b019313540c418e639a75e9c6ed1a7caa9351a
