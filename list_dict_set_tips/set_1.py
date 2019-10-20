from random import randint

s = set([randint(-10, 10) for _ in range(10)])
print(s)

# 要求找到集合中能被2整除的子集
ret = {x for x in s if x % 2 == 0}
print(ret)
