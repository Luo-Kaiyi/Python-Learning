food_order = ['鸡爪','鸭爪','鸡翅','鸭翅','鸡腿','牛肉']
print("牛肉卖完了！")
finished_order = []
while food_order:
    food = food_order.pop()
    if food != '牛肉':
        print("给你一个" + food)
        finished_order.append(food)
    else:
        print("不好意思，牛肉已经卖完了！")
print("现在，你有这些熟食了：")
while finished_order:
    food = finished_order.pop()
    print(food)