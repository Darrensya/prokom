from random import randint


class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


d6 = Die()
d10 = Die(10)
d20 = Die(20)

for die in (d6, d10, d20):
    print(f"\n10 rolls dari {die.sides}-sided die:")
    for _ in range(10):
        die.roll_die()