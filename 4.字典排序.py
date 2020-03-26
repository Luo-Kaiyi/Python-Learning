from random import randint
d = {x: randint(50, 100) for x in 'abcdefgh'}
print(d)
print(sorted(d))
print(iter(d))
print(list(iter(d)))
d2 = list(zip(d.values(), d.keys()))  # 使用zip函数，得到一个键值位置互换的新列表
print(sorted(d2))
print(dict(sorted(d2)))
print('#'*50)

print(d.items())
print(sorted(d.items(), key=lambda x: x[1]))
print(dict(sorted(d.items(), key=lambda x: x[1])))