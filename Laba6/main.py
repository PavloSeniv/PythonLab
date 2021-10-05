# Task Module
from radius_and_pow import radius_pow

res2 = radius_pow.my_pow2(2.0)
print("Піднесення до квадрату:", res2)

res3 = radius_pow.my_pow3(2.0)
print("Піднесення до кубу:", res3)

diagonal_square= radius_pow.diagonal(2)
print("Діагональ квадрату:", diagonal_square)

perimeter_square = radius_pow.perimeter(2)
print("Периметр квадрату:", perimeter_square)

square_area = radius_pow.square(2)
print("Площа квадрату:", square_area)

radius_circle_inscribed_square = radius_pow.radius_circle(2)
print("Радіус кола вписаного в квадрат:", radius_circle_inscribed_square)

#########################################

# Task generator
print()

kn_2_file = "KN-2.csv"
lines = [line for line in open(kn_2_file)]
for i in lines:
    # print(i)
    continue

list_line = (s.rstrip().split(",") for s in lines)
next(list_line)

student_1 = next(list_line)
student_2 = next(list_line)
student_3 = next(list_line)
student_4 = next(list_line)
student_5 = next(list_line)
student_6 = next(list_line)
student_7 = next(list_line)

student_list = [student_1,student_2,student_3,student_4,student_5,student_6,student_7]
# print(student_list)

while True:
    for student_item in student_list:
        student = student_item
    surname_student = student[0]
    lab1 = student[1]
    if lab1 == '+':
        lab1 = 2
    else:
        lab1 = 0

    lab2 = student[2]
    if lab2 == '+':
        lab2 = 2
    else:
        lab2 = 0

    lab3 = student[3]
    lab3 = list(lab3)
    lab3 = int(lab3[0]) + int(lab3[2])
    # print(lab3)

    test = int(student[4])
    test_20 = test / 5
    test = test_20
    # print(test)

    kr1 = int(student[5])

    sum_all_points = str(lab1 + lab2 + lab3 + test + kr1)
    # print(sum_all_points)

    student_result = open('student_result.txt', 'wt')
    student_result.write(surname_student + "|")
    student_result.write(sum_all_points)
    break
print("Работа закінчена")