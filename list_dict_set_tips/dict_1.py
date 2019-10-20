from random import randint

data = {x: randint(60, 100) for x in range(1, 20)}
print(data)

# 字典的意义是学号：分数，要求过滤出分数高于90的
ret = {k: v for k, v in data.items() if v > 90}
print(ret)
