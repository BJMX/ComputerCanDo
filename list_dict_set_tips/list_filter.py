from timeit import timeit

# 生成随机列表
from random import randint

data = [randint(-10, 10) for _ in range(10)]
print("data={}".format(data))

res = filter(lambda x: x < 0, data)
print("below 0 number are: {}".format(list(res)))

print(timeit(stmt="filter(lambda x:x<0, data)", setup="from random import randint;data=[randint(-10, 10) for _ in range(10)]", number=20))
