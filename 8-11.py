def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians, new_magicians):
    while magicians:
        magician = magicians.pop() + ' the Great'
        new_magicians.append(magician)

list_magicians = ['Aditya', 'Donato', 'Vixey']
new_list_mag = []

make_great(list_magicians[:], new_list_mag)
show_magicians(list_magicians)
show_magicians(new_list_mag)