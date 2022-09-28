from random import choice
students = []
for i in range(4):
    a = str(input('Student: '))
    students.append(a)
b = choice(students)
print('The chosen student was: {}'.format(b))
