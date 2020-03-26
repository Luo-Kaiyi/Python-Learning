place1 = ['wuhan', 'chongqing', 'shanghai']
place2 = ['guilin', 'beijing', 'hainan']
palce3 = ['chengdu', 'guangzhou']
favorite_places = {'shen': place1, 'zhang': place2, 'luo': palce3}
for name,places in favorite_places.items():
    for place in places:
        print(name.title() + " likes " + place.title() + ".")