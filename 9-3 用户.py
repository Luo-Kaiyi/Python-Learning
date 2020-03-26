class User:
    def __init__(self, first, last, age, gender="male"):
        self.first_name = first
        self.last_name = last
        self.age = age
        self.gender = gender

    def profile(self):
        profile = "First name: " + self.first_name.title() + "\nLast name: " + self.last_name.title() + "\nGender: " + self.gender + \
                  '\nAge: ' + str(self.age) + "\n"
        return profile

    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title() + " !")


user1 = User('chou', 'jay', 30)
user2 = User('helen', 'keller', 25, 'female')
user3 = User('he', 'yu', 20)

user1.greet_user()
user2.greet_user()
user3.greet_user()
print("\n")
print(user1.profile())
print(user2.profile())
print(user3.profile())