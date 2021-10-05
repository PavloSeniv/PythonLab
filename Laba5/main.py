# Task 1.1
# input_namber = input("Введіть число:")
# sum_namber = sum([int(i) for i in input_namber])
# print("Сума цифр числа:", sum_namber)

##################################################

# Task 1.2
# companies = ["Microsoft", "Google", "Oracle", "Apple","Apple"]
# for item in companies:
#     print(item)
# companies_count = companies.count(item)
# if companies_count >= 2:
#   print("Елемент не унікальний")

##################################################

# Task 1.3
# string = str(input())
# array = string.split(" ")
# count = 0
# for i in array:
#     if len(i) > 1:
#         count += 1
# print(count)

##################################################

# Task 1.4
# message = input("Введіть текст: ")
# value_vowels = "аоеиуі"
# count = 0
# for letter in message:
#      if letter.lower() in value_vowels:
#          count += 1
# print("Голосних букв у тексті: ", count)

##################################################

# Task 2.1
# dict_abc = {'a': 1, 'b': 2, 'c': 3, 'd': 3}
# dict_123 = {v: k for k, v in dict_abc.items()}
# print(dict_123)

##################################################

# Task 2.2
# import random
# student_surname = ("Seniv", "Dybrovskyi", "Chomei", "Kucher", "Morozov")
# i = 0
# while i < len(student_surname):
#     print(student_surname[i])
#     i += 1

# student_point_list = [] # спочатку пустий список
# i_1 = 0
# while i_1 < i:
#     num = random.randint(1,100)
#     student_point_list = student_point_list + [num]
#     i_1 = i_1+1

# student_surname_list= list(student_surname)

# student_all = { ssl:spl for (ssl,spl) in zip(student_surname_list,student_point_list) }
# print(student_all)

##################################################

# Task 2.3
# char_01 = "01"

##################################################

# Task 2.4
# string_word = "hello world qwerty world hello"
# string_dict = dict.fromkeys(string_word)
# print(string_dict)
##################################################