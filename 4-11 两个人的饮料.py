my_drinks = ['baixiangguo','shuangxiangpao','mitaojingqiu','pepsi']
friend_drinks = my_drinks[:]
my_drinks.append('juice')
friend_drinks.append('milktea')
print("My favorite drinks are:")
for drink in my_drinks:
    print(drink)
print("My friend's favorite drinks are:")
for drink in friend_drinks:
    print(drink)