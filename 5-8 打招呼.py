names = ['admin','Eric','Jack','Alice','Cristin']
for name in names:
    if name == 'admin':
        print("Hello " + name + ", would you like to see a status report?")
    else:
        print("Hello " + name + ", thank  you for logging in again.")

while names != []:
    names.pop()
if names == []:
    print("We need to find some users.")