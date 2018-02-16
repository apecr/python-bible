import random


class Coin:
    def __init__(self, rare=False, clean=True, heads=True, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.heads = heads
        self.is_rare = rare
        self.is_clean = clean
        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value
        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def __del__(self):
        print('Coin Spent!')

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def flip(self):
        self.heads = random.choice([True, False])


class Pound(Coin):
    def __init__(self):
        data = {
            'original_value': 1.00,
            'clean_color': 'gold',
            'rusty_colour': 'greenish',
            'num_edges': 1,
            'diameter': 22.5,
            'thichness': 3.15,
            'mass': 9.5
        }
        super().__init__(**data)

