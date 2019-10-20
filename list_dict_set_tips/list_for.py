# 查找输出data中所有小于0的数
data = [1, 3, -4, 2, -8, -1, 0, 9]

res = []

for i in data:
    if i < 0:
        res.append(i)

print(res)
