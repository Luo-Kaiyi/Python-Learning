from random import randint
from collections import deque
import json
# 猜数字游戏
N = randint(0,99)
history = deque([],5)

def guess(n):
    if n == N:
        print('Right!')
        return True
    elif n < N:
        print(str(n) + ' is less than N!')
    else:
        print(str(n) + ' is greater than N!')
    return False


while True:
    k = input("Guess a number:\t")
    if k.isdigit():
        n = int(k)
        history.append(n)
        if guess(n):
            break
    elif k == 'history' or k == 'h':
        print(list(history))

json.dump(str(history), open('History','w'))
q = json.load(open('History'))
print(q)