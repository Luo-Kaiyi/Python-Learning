def make_cars(producer, model, **car_info):
    cars = {'producer_name': producer, 'car_model': model, }
    for key, value in car_info.items():
        cars[key] = value
    return cars


car1 = make_cars('BWM', '730', color='white', price='$200000')
car2 = make_cars('Audi', 'R8', color='grey')
print(car1)
print(car2)