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
import csv

def parse_file(data_csv):
  for row_student in data_csv:
    print(row_student)
    row_student['Lab1'] = 2 if row_student['Lab1'] in '+' else 0
    row_student['Lab2'] = 2 if row_student['Lab2'] in '+' else 0
    row_student['Lab3'] = sum(int(i) for i in str(row_student['Lab3']).split('/'))
    row_student['Test'] = int(row_student['Test']) / 5
    row_student['KR1'] = int(row_student['KR1'])
    
def sum_all_points(row_student):
  return {'Name': row_student['Student'], 'Points': row_student['Lab1'] + row_student['Lab2'] + row_student['Lab3'] + row_student['Test'] + row_student['KR1']}

data_csv  = list(row_student for row_student in csv.DictReader(open("KN-2.csv")))
parse_file(data_csv)
student_result_zalik = list(sum_all_points(row_student) for row_student in data_csv)

with open('student_result.txt', 'w') as student_result:
  for row_student in student_result_zalik:
    a = student_result.writelines(f"|| {row_student['Name'].ljust(15)} | {row_student['Points']} || \n")
