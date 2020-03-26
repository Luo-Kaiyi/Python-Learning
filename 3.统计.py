from random import randint
from collections import Counter
s = [randint(1, 10) for x in range(21)]
print(s)
c = dict.fromkeys(s, 0)
print(c)
for i in s:
    c[i] += 1
print(c)
c1 = Counter(c)
print(c1)
c2 = c1.most_common(5)
print(c2)
