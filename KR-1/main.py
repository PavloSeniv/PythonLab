<<<<<<< HEAD
# V-10

# Task1
# s = input().split() # Приклад: Сьогодні на вулиці холодно або ні
# k=0
# for i in s:
#     if i.count('а')>0:
#         k+=1
# print(k)

# Task2

# Task 3
# class Iteration:
#   def __init__(self,end):
#     self.number = 1
#     print(self.number)
#     self.end=end
#   def __iter__(self):
#     return self
#   def __next__(self):
#     if self.number>=self.end:
#       raise StopIteration
#     self.number = self.number + (self.number + 2) -1
#     return self.number

# d=Iteration(4) # Початок, крок, кінець проміжку
# for i in d:
#   print(i)

# Task4
class Instructor:
    def __init__(self, name, surname, semester):
        self.name = name
        self.surname = surname
        self.semester = semester

    def __str__(self):
        return f'{self.name} {self.surname} {self.semester}'


    def count_sem(self, semester):
       return len(self.semester[semester])

    def marks_average(self, semester):
        return len(self.semester[semester]) / len(self.semester[semester])

instructor = Instructor('Pablo', 'Seniv', {
    1: ["Taml", "C++", "Python"],
    2: ["Taml2", "C++", "Python","Python1"]
})

print(str(instructor))
print('Sem1 - ' + str(instructor.count_sem(1)))
print('Sem_1- ' , instructor.marks_average(1))

>>>>>>> 22b019313540c418e639a75e9c6ed1a7caa9351a
