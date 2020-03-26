foods = ['鸡爪','鸭爪','鸡翅','鸭翅','鸡腿','牛肉']
bag = []
while foods:
    food = foods.pop()
    print("给你一个" + food + '.')
    bag.append(food)
print("现在，你有这些熟食了：")
while bag:
    food = bag.pop()
    print(food)