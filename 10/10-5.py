filename = 'programming_reasons.txt'

while True:
    reason = input("Why do you like Programming? (Press q to quit) ")
    if reason != 'q':
        with open(filename, 'a') as file_object:
            file_object.write(reason + '\n')
    else:
        break