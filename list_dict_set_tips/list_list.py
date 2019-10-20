from random import randint
from timeit import timeit

data = [randint(-10, 10) for _ in range(10)]
print("data = {}".format(data))

res = [i for i in data if i < 0]
print("below 0 numbers are: {}".format(list(res)))

print(timeit(stmt="[i for i in data if i < 0]", setup="from random import randint;data=[randint(-10, 10) for _ in range(10)]", number=20))
