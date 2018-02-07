# NAME = 0
# AGE = 1
# SEX = 2
# EMAIL = 3
# # 或者通过这样定义
# s =NAME,AGE,SEX,EMAIL = range(4)
# print(s)
from collections import namedtuple
Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])
s = Student('Jim', 21, 'male', '123@qq.com')
print(s.name)

print(s.age)
print(s)

import time
time.localtime()
