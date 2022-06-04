filenames = ['siddhartha.txt', 'belfort.txt', 'eegweg.txt']
for filename in filenames:
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print("Sorry. The file is missing.")
    else:
        count = contents.lower().count('the')
        print(filename + " contains " + str(count) + " thes.")