def describe_city(city_name, country='China'):
    return '"' + city_name.title() + ", " + country.title() + '"'


print(describe_city('chengdu'))
print(describe_city('los angeles', 'america'))
print(describe_city('london', 'english'))