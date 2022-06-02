filename = 'guest_book.txt'

flag = True
while flag:
    name = input('What is your name? (Press q to quit) ')
    if name != 'q':
        visit = "Welcome, " + name + '!'
        print(visit)
        with open(filename, 'a') as file_object:
            file_object.write(visit + '\n')
    else: 
        break