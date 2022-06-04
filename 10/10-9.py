filenames = ['cats.txt','ogs.txt']

for filename in filenames:
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
            print(contents)
    except FileNotFoundError:
        pass