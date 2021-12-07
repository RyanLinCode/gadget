from random import randint

class Dice:
    def __init__(self, rum_sides = 6):
        self.num_sides = rum_sides

    def roll(self):
        return randint(1, self.num_sides)


