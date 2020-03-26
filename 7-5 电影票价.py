age = input("Please enter your age (enter '-1' to end):\n")
age = int(age)
active = True
while active:
    if age < 3:
        print("Your ticket is free!")
    elif age < 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")
    age = input("Please enter your age (enter '-1' to end):\n")
    age = int(age)
    if age == -1:
        active = False
