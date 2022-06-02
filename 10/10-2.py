filename = '10-1.txt'
with open(filename) as file_object:
    contents = file_object.readlines()

for line in contents:
    modified_line = line.replace('Python', 'C')
    print(modified_line.rstrip())