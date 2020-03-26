def make_sandwich(*toppings):
    print("Your sandwich has :")
    for topping in toppings:
        print('-' + topping)


make_sandwich('chicken', 'ham', 'vegetable')
make_sandwich('steak')
make_sandwich()