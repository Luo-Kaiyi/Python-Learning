def show_magicians(mag):
    for magician in mag:
        print("Hello, magician " + magician.title() + ".")


def make_great(mag):
    great_list = []
    while mag:
        magician = mag.pop()
        magician = 'the Great ' + magician
        great_list.append(magician)
    return great_list


magicians = ['xu', 'dec', 'chou', 'sil']
show_magicians(magicians)
great_magicians = make_great(magicians[:])
show_magicians(magicians)
show_magicians(great_magicians)