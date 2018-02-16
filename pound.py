import random

class Pound:
    def __init__(self, rare=False):
        self.rare = rare
        self.value = 1.00
        if self.rare:
            self.value = 1.25
        self.colour = 'gold'
        self.num_edges = 1
        self.diameter = 22.5 # mm
        self.thickness = 3.15 # mm
        self.heads = True

    def __del__(self):
        pint('Coin Spent!')

    def rust(self):
        self.colour = 'greenish'

    def clean(self):
        self.colour = 'gold'

    def flip(self):
        self.heads = random.choice([True, False])

