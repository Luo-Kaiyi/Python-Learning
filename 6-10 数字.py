num1 = (1, 3, 4, 8)
num2 = (4, 7, 3, 5)
num3 = (1, 5, 8, 9)
num4 = (2, 6, 8)
num5 = (7, 8)
favorite_numbers = {'lee': num1, 'luo': num2, 'He': num3, 'yu': num4, 'ling': num5}
for name, nums in favorite_numbers.items():
    print(name.title() + " likes number:")
    for num in nums:
        print(num)