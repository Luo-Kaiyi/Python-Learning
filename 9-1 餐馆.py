class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.cuisine_type = type
        self.number_served = 0

    def describe_restaurant(self):
        describe = "餐馆名字：" + self.name + "\t菜式：" + self.cuisine_type + "。"
        return describe

    def open_restaurant(self):
        print("餐馆" + self.name + "正在营业！")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, inc):
        self.number_served += inc


restaurant1 = Restaurant("海底捞", "火锅")
print("1. 在这家餐厅就过餐的人数为：" + str(restaurant1.number_served))
restaurant1.set_number_served(5)
print("2. 在这家餐厅就过餐的人数为：" + str(restaurant1.number_served))
restaurant1.increment_number_served(100)
print("3. 在这家餐厅就过餐的人数为：" + str(restaurant1.number_served))