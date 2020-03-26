from random import randint, sample

d = sample('abcde', randint(3, 6))
print(d)
d1 = {i: randint(1, 10) for i in sample('abcdefgh', randint(3, 6))}
print(d1)
d2 = {i: randint(1, 10) for i in sample('abcdefgh', randint(3, 6))}
print(d2)
d3 = {i: randint(1, 10) for i in sample('abcdefgh', randint(3, 6))}
print(d3)
print(d1.keys() & d2.keys() & d3.keys())

s = list(map(dict.keys, [d1, d2, d3]))
print(s)