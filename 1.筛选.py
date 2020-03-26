from random import randint

data = [randint(-20, 20) for i in range(10)]
print(data)
d1 = list(filter(lambda x: x >= 0, data))  # 使用filter函数筛选数据
print(d1)
d2 = [x for x in data if x >= 0]  # 使用列表解析筛选
print(d2)
print("#"*50)

data2 = {x: randint(50, 100) for x in 'abcdefghij'}
print(data2)
d3 = {k: v for k, v in data2.items() if v >= 85}
print(d3)

data3 = set(data)
print(data3)
d4 = {x for x in data3 if x % 3 == 0}
print(d4)
d5 = set(filter(lambda x: x % 3 == 0, data3))
print(d5)