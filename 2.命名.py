from collections import namedtuple


student = ('Ferry', 'male', '18', '13456@gmail.com')
NAME, SEX, AGE, EMAIL = range(4)
print(student[NAME])
print(student[SEX])
print(student[AGE])
print(student[EMAIL])

Student = namedtuple('Student', ['name', 'sex', 'age', 'email'])
s = Student('Ferry', 'male', '18', '13456@gmail.com')
print(s)
print(s.name)
print(s.sex)
print(isinstance(s,tuple))