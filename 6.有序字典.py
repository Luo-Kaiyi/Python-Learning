from collections import OrderedDict
from time import time
from random import randint

d = OrderedDict()
players = list('ABCDEFGH')
start = time()   # 使用time函数计时

for i in range(8):
    input()
    p = players.pop(randint(0, 7-i))   # 随机弹出一个
    end = time()   # 计时结束
    print(str(i+1) + '. ' + p + ' ' + str(end-start))
    d[p] = (i+1, end-start)
print(dict(d))
