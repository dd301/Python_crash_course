def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians, new_magicians):
    while magicians:
        magician = magicians.pop() + ' the Great'
        new_magicians.append(magician)

list_magicians = ['Aditya', 'Donato', 'Vixey']
new_list_mag = []
show_magicians(list_magicians)
make_great(list_magicians, new_list_mag)
print(new_list_mag)