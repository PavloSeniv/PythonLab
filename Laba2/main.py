# List
# Task 1
# a = []
# for i in range(int(input())):
#  a.append(int(input()))
# print(a)
# length_a = len(list(a))
# print('Length: ' +  str(length_a))
# last_user = a[-1]
# a.remove(last_user)
# print(a)

##################################################

# Task 2
# from random import randrange
# a1=[]
# n = int(input())
# for i in range(n):
#   a1.append(randrange(1, 10))
# print(a1)
# sum_list = a + a1
# print(sum_list)

##################################################

# Task 3
# word = str(input())
# list_word = list(word)
# print(list_word)

##################################################

# Error exclusion
# Task 1
# try:
#   x = int(input("Введіть число x: "))
#   result = 1 / x
#   print('Результат ділення 1 / x: ' +  str(result))
# except ZeroDivisionError:
#   print('Ділити на нуль не можна!!!')
# finally:
#   print('Програма завершила свою роботу)')

##################################################

# Main Task
# from random import randrange

# print("My menu")
# print("1: create list")
# print("2: add element")
# print("3: preview")
# print("4: exit")
# print("-1: create list(range(у))")
# print("-2: del element[i]")

# while True:
#     try:
#         number_menu = int(input("Ваші дії: "))
#         if number_menu == 1:
#             list_a = []
#             print("Done")
#         if number_menu == 2:
#             try:
#                 element_a = int(input("Element: "))
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
#         if number_menu > 4:
#             print("Дане число не належить пункту меню")
#         if number_menu == -1:
#             list_a = []
#             y = int(input("Введіть розмір списку: "))
#             for i in range(y):
#                 list_a.append(randrange(1, 10))
#         if number_menu == -2:
#             del_el_list = int(
#                 input("Введіть індекс елемента, який потрібно видалити: "))
#             list_a.pop(del_el_list)
#     except ValueError:
#         print("Необхідно задати число!")

##################################################

# Dist Task
# city = {
#     "Berlin": "Germany",
#     "Russia": "Moscow",
#     "Kiev": "Ukraine",
#     "Minsk": "Belarus",
#     "Washington": "USA",
#     "Rome": "Italy"
# }

# key = str(input("Введіть назву міста: "))

# if key in city:
#     city_dict = city[key]
#     print("Місто знаходиться в країні: " + city_dict)
# else:
#     print("Місто не знайдено")

# list_city = list(city.keys())
# print("Утворений список: " + str(list_city))

# lentgh_city = len(city)
# print("К-сть елементів словника: " + str(lentgh_city))

# key_city = str(input("Введіть назву міста, для видалення: "))
# if key_city in city:
#     del_city = city.pop(key_city)
#     print("Видалено місто " + str(key_city) + ", яке знаходить в країні " +
#           str(del_city))
# else:
#     print("Місто не знайдено")

# list_city_2 = list(city.values())
# print("Новоутворений список: " + str(list_city_2))

# add_city = str(input("Введіть назву міста для додавання: "))
# add_сountry = str(input("Введіть назву країни для додавання: "))
# new_city = dict({add_city: add_сountry})
# city.update(new_city)
# print("Обновлений словник: " + str(city))

##################################################

# Dist Task menu
# from random import randrange

# print("My menu")
# print("1: create dist")
# print("2: add element")
# print("3: preview")
# print("4: exit")
# print("-1: create dist Create a list of words that break into a dictionary")
# print("-2: del element[i]")

# while True:
#     try:
#         number_menu = int(input("Ваші дії: "))
#         if number_menu == 1:
#             dist_a = {}
#             print("Done")
#         if number_menu == 2:
#             try:
#                 add_key = str(input("Введіть ключ: "))
#                 if add_key in dist_a:
#                     new_dist_key = dist_a[add_key]
#                     if new_dist_key == new_dist_key:
#                         print("Такий ключ вже існує в словнику")
#                 else:
#                     add_val = str(input("Введіть значення: "))
#                     new_dist = dict({add_key: add_val})
#                     dist_a.update(new_dist)
#             except:
#                 print("Створіть спочатку словник")
#         if number_menu == 3:
#             try:
#                 print(dist_a)
#             except:
#                 print("Створіть спочатку словник")
#         if number_menu == 4:
#             break
#         if number_menu > 4:
#             print("Дане число не належить пункту меню")
#         if number_menu == -1:
#             dist_a = {}
#             dist_word = input("Введіть ключове слово:")
#             dist_a = {sym: sym * randrange(1, 10) for sym in dist_word}
#         if number_menu == -2:
#             del_key = str(input("Введіть ключ: "))
#             del dist_a[del_key]
#     except ValueError:
#         print("Необхідно задати число!")