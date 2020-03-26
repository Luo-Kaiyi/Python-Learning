city1 = {'country': 'french', 'population': 'middle amount', 'fact': 'a romantic city'}
city2 = {'country': 'china', 'population': 'small amount', 'fact': 'a peaceful city'}
city3 = {'country': 'america', 'population': 'large amount', 'fact': 'a developed city'}
cities = {'paris': city1, 'meishan': city2, 'new york': city3}
for name,city in cities.items():
    print(name.title() + " is " + city['fact'] + ", located in " + city['country'].title() +
          " with " + city['population'] + " of people.")