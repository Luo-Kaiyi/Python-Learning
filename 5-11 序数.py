orders = list(range(1,10))
for order in orders:
    if order == 1:
        print("\t" + str(order) + "st")
    elif order == 2:
        print("\t" + str(order) + "nd")
    elif order == 3:
        print("\t" + str(order) + 'rd')
    else:
        print("\t" + str(order) + "th")