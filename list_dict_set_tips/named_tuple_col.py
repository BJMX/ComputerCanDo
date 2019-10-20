from collections import namedtuple

# 本质是创建的一个类
Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])
s = Student('jim', 16, 'male', 'jim1234@gmail.com')

print(s.name, s.sex, s.email)
