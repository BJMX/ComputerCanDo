from collections import Counter
from random import randint

data = [randint(0, 20) for _ in range(30)]
print(data)

c = Counter(data)
print(c)

# 找出频度出现最高的3个数
print(c.most_common(3))

