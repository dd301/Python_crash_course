from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        print(randint(1, self.sides))

die6 = Die()
i = 0
print("\n6-sided die:")
while i < 5: 
    die6.roll_die()
    i += 1

die10 = Die(10)
print("\n10-sided die:")
while i < 10:
    die10.roll_die()
    i += 1

die20 = Die(20)
print("\n20-sided die:")
while i < 15:
    die20.roll_die()
    i += 1