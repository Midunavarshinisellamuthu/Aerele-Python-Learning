from collections import namedtuple
Student=namedtuple('Student',['name','age'])
s=Student('Midu',20)
print(s.name)
print(s.age)