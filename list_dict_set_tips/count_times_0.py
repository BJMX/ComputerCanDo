from random import randint

data = [randint(0, 20) for _ in range(30)]
print(data)

c = dict.fromkeys(data, 0)
# print(c)

for x in data:
    c[x] += 1

print(c)
