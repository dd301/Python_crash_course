import json

filename = 'fav_num.json'

try:
    with open(filename) as f_obj:
        num = json.load(f_obj)
        print("I know your favourite number! It's " + num)
except FileNotFoundError:
    fav_num = input("What is your favourite number? ")
    with open(filename, 'w') as f_obj:
        json.dump(fav_num, f_obj)