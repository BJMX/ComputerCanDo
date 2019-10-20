# 字典根据值排序
from random import randint

d = {i:randint(60, 100) for i in "xyzabc"}
print(d)
# 1.设置sorted函数的key参数为字典的值
print(sorted(d.items(), key=lambda x: x[1]))

# 2.zip转成元组再进行比较
t = list(zip(d.values(), d.keys()))
print(t)

# t = [(91, 'x'), (68, 'y'), (72, 'z'), (69, 'a'), (80, 'b'), (83, 'c')]
print(sorted(t))

