# Task 1
# number_x = int(input())

##################################################

# Task 2
# print('Task 2: ' + str(number_x))

##################################################

# Task 3
# number_x = int(input())
# sum_x = float(number_x+0.8)
# print('Task 3: ' + str(sum_x))

##################################################

# Task 4
# number_x = int(input())
# string_x = str(number_x)
# print(string_x*3)

##################################################

# Task 5
# print('Enter number < 100: ')
# number_x = str(int(input()))
# last_number = int(number_x[len(number_x)-1])
# first_number = int(number_x[len(number_x)-len(number_x)])
# print(first_number)
# string = 'Zalik zdalo '
# if last_number == 0 or last_number == 5 or last_number == 6 or last_number == 7 or \
#         last_number == 8 or last_number == 9 or first_number == 1:
#     string += number_x + ' studeniv'
# elif last_number == 2 or last_number == 3 or last_number == 4:
#     string += number_x + ' studenty'
# elif first_number == 1:
#     string += number_x+' student'
# print(string)

##################################################

# Task 6
# import math
# print('Enter 2 numbers > 0')
# number_a = float(input("Number a: "))
# number_b = float(input("Number b: "))
# if number_a < 0 and number_a < 0 :
#     print('Enter number > 0')
# else:
#     x = math.sqrt(number_a * number_b) / (math.exp(number_a) * number_b) + number_a*math.exp((2*number_a)/number_b)
#     print("Result: " + str(x))

##################################################

# Task 7
# number_n = int(input())
# number_x = float(input())
# result = 1
# for i in range(1, number_n+1):
#     result += pow(number_x, i)
# print(result)

##################################################

# Task 8
# number_n = int(input())
# number_d = 2
# if number_n == 1:
#     print('Prime number')
# else:
#     while number_n % number_d != 0:
#         number_d += 1
#     if number_d == number_n:
#         print('Prime number')
#     else:
#         print('Not prime number')

##################################################

# Task 9
#import random
# number_zero = 0;
# while number_zero<10:
#     print(random.randint(1,1000))
#     number_zero+=1

##################################################

# Task 10
# import random
# result = 0
# answer = ''
# while result != answer:
#    number_1 = random.randint(1, 10)
#    number_2 = random.randint(1, 10)
#    result = number_1*number_2
#    print(str(number_1)+" * "+str(number_2)+" = ")
#    answer = int(input())
# print("Answer is right!")
