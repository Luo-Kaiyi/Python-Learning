favorite_language = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
list = ['jen', 'sarah', 'jack', 'edward', 'vott', 'phil']
for name in list:
    if name in favorite_language.keys():
        print("Thank you, " + name + ".")
    else:
        print("Please participate in our survey, " + name + '.')